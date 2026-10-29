#!/usr/bin/env python3
"""Discover verification candidates and run explicit project verification contracts.

Only ``run`` executes project commands. Discovery never treats a script or CI
snippet as approved verification. This module uses only the Python standard
library; command argument vectors are executed without a shell.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import time
from typing import Any


PLATFORMS = {"darwin", "linux", "win32"}
PHASES = ("health", "interaction", "checks", "cleanup")


class VerificationError(ValueError):
    """The contract or requested evidence location cannot be used safely."""


def _root(root: str | Path) -> Path:
    path = Path(root).resolve()
    if not path.is_dir():
        raise VerificationError(f"Project root is not a directory: {path}")
    return path


def discover(root: str | Path) -> dict[str, Any]:
    """Inventory repository facts and command candidates without executing them."""
    root = _root(root)
    packages = []
    package_paths = {root / "package.json"}
    package_path = root / "package.json"
    if package_path.is_file():
        package = json.loads(package_path.read_text(encoding="utf-8"))
        workspaces = package.get("workspaces", [])
        if isinstance(workspaces, dict):
            workspaces = workspaces.get("packages", [])
        if isinstance(workspaces, list):
            for pattern in workspaces:
                if isinstance(pattern, str) and not Path(pattern).is_absolute() and ".." not in Path(pattern).parts:
                    for folder in root.glob(pattern):
                        candidate = folder / "package.json"
                        if candidate.is_file() and candidate.resolve().is_relative_to(root):
                            package_paths.add(candidate)
    for path in sorted(package_paths):
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            packages.append({"path": str(path.relative_to(root)), "scripts": data.get("scripts", {})})
    workflows = []
    for path in sorted((root / ".github/workflows").glob("*")):
        if path.suffix in {".yml", ".yaml"} and path.is_file():
            clues = [{"line": index, "text": line.strip()} for index, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ) if re.match(r"\s*(?:-\s*)?(?:runs-on|run|uses|if|needs|services):", line)]
            workflows.append({"path": str(path.relative_to(root)), "clues": clues})
    configs = [name for name in ("pyproject.toml", "tox.ini", "pytest.ini", "Makefile", "justfile",
               "Cargo.toml", "go.mod", "compose.yaml", "compose.yml", "docker-compose.yml",
               "requirements.txt", "package-lock.json", "pnpm-lock.yaml", "yarn.lock") if (root / name).is_file()]
    docs = sorted({str(path.relative_to(root)) for pattern in ("README*", "AGENTS.md", "CONTRIBUTING*")
                   for path in root.glob(pattern) if path.is_file()})
    return {"version": 1, "project": root.name, "candidate_only": True,
            "packages": packages, "workflows": workflows, "configs": configs, "documentation": docs}


def scaffold(root: str | Path) -> dict[str, Any]:
    """Return an intentionally incomplete contract for a human/agent to finish."""
    root = _root(root)
    return {"version": 1, "project": root.name, "launch": None, "health": [],
            "interaction": [], "checks": [], "cleanup": [], "ci_exceptions": []}


def _validate_command(command: Any, location: str) -> None:
    if not isinstance(command, dict):
        raise VerificationError(f"{location} must be a command object")
    if set(command) - {"name", "argv", "timeout_seconds", "platforms"}:
        raise VerificationError(f"{location} contains unsupported command fields")
    if not isinstance(command.get("name"), str) or not command["name"].strip():
        raise VerificationError(f"{location}.name must be nonempty")
    argv = command.get("argv")
    if not isinstance(argv, list) or not argv or any(not isinstance(arg, str) or "\0" in arg for arg in argv) or not argv[0]:
        raise VerificationError(f"{location}.argv must be a nonempty string argument vector")
    timeout = command.get("timeout_seconds")
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise VerificationError(f"{location}.timeout_seconds must be finite and positive")
    if "platforms" in command:
        platforms = command["platforms"]
        if not isinstance(platforms, list) or not platforms or any(not isinstance(p, str) or p not in PLATFORMS for p in platforms):
            raise VerificationError(f"{location}.platforms must name supported Python platforms")


def validate_manifest(data: Any) -> dict[str, Any]:
    """Validate all phases before any project command is executed."""
    fields = {"version", "project", "launch", *PHASES, "ci_exceptions"}
    if not isinstance(data, dict) or set(data) != fields:
        raise VerificationError("Contract must contain exactly version, project, launch, health, interaction, checks, cleanup, ci_exceptions")
    if type(data["version"]) is not int or data["version"] != 1:
        raise VerificationError("Unsupported contract version")
    if not isinstance(data["project"], str) or not data["project"].strip():
        raise VerificationError("project must be nonempty")
    if data["launch"] is not None:
        _validate_command(data["launch"], "launch")
    for phase in PHASES:
        commands = data[phase]
        if not isinstance(commands, list) or not commands:
            raise VerificationError(f"{phase} must contain at least one explicit command")
        for index, command in enumerate(commands):
            _validate_command(command, f"{phase}[{index}]")
    exceptions = data["ci_exceptions"]
    if not isinstance(exceptions, list) or any(not isinstance(item, dict) or set(item) != {"job", "reason"}
            or any(not isinstance(item[key], str) or not item[key].strip() for key in ("job", "reason")) for item in exceptions):
        raise VerificationError("ci_exceptions must contain nonempty job and reason strings")
    return data


def generate_skill(root: str | Path, manifest: dict[str, Any], output_dir: str | Path, force: bool = False) -> Path:
    """Write a self-contained skill containing the explicit portable contract."""
    _root(root)
    validate_manifest(manifest)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    path = output / "SKILL.md"
    description = json.dumps(f"Verify {manifest['project']} with its recorded project commands and outcome evidence.")
    content = f'''---
name: project-verification
description: {description}
---

# Project Verification

Use this contract from the project root after checking its commands still match
the current repository. Argument vectors are executed directly, without a shell.
Resolve project paths relative to that root; use the project's recorded runtime.

Launch the optional long-lived process, then establish health before interaction.
Run the interaction and local CI checks with the recorded timeouts. Always run
cleanup and terminate the launched process and its children, including on failure.
For a project without a service or teardown, keep an explicit harmless health or
cleanup command documenting that fact rather than silently dropping the phase.

Record the exact Git revision, dirty state, command results, product observations,
and evidence locations. Unsupported platforms or CI exceptions are INCONCLUSIVE;
failed commands are FAIL. A command PASS alone does not establish product intent.
Return to the original acceptance criteria for the final product verdict.

```json
{json.dumps(manifest, indent=2, ensure_ascii=False)}
```
'''
    try:
        with path.open("w" if force else "x", encoding="utf-8") as handle:
            handle.write(content)
    except FileExistsError as exc:
        raise VerificationError(f"Skill already exists: {path}; use --force to replace it") from exc
    return path


def _git_state(root: Path) -> dict[str, Any]:
    repository_root = root

    def git(*args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(["git", "-C", str(repository_root), *args], capture_output=True, timeout=10)
    try:
        toplevel = git("rev-parse", "--show-toplevel")
        if toplevel.returncode:
            return {"head": None, "dirty": None, "error": "No Git working tree available"}
        # Remove Git's one line terminator, not whitespace belonging to the path.
        location = toplevel.stdout[:-1] if toplevel.stdout.endswith(b"\n") else toplevel.stdout
        repository_root = Path(os.fsdecode(location)).resolve()
        identity = {"project_root": str(root), "repository_root": str(repository_root), "mode": "worktree"}
        head = git("rev-parse", "--verify", "HEAD")
        if head.returncode:
            return {**identity, "head": None, "dirty": None, "error": "No Git HEAD available"}
        status = git("status", "--porcelain=v1", "--untracked-files=all", "-z")
        diff = git("diff", "--no-ext-diff", "--no-textconv", "--binary", "HEAD", "--")
        index = git("ls-files", "--stage", "-z")
        if status.returncode or diff.returncode or index.returncode:
            return {**identity, "head": head.stdout.decode().strip(), "dirty": None, "error": "Git worktree state unavailable"}
        digest = hashlib.sha256(status.stdout + diff.stdout + index.stdout)
        for entry in index.stdout.split(b"\0"):
            if entry:
                metadata, name = entry.split(b"\t", 1)
                path = repository_root / os.fsdecode(name)
                digest.update(name)
                try:
                    mode = path.lstat().st_mode
                    digest.update(f"\0{stat.S_IFMT(mode):o}:{mode & 0o111:o}\0".encode())
                except FileNotFoundError:
                    digest.update(b"\0missing\0")
                if metadata.startswith(b"160000 ") and any(item[3:] == name for item in status.stdout.split(b"\0") if len(item) >= 3):
                    return {**identity, "head": head.stdout.decode().strip(), "dirty": None,
                            "error": "Dirty submodule contents require separate verification"}
        untracked = git("ls-files", "--others", "--exclude-standard", "-z")
        if untracked.returncode:
            return {**identity, "head": head.stdout.decode().strip(), "dirty": None, "error": "Git untracked state unavailable"}
        for name in untracked.stdout.split(b"\0"):
            if name:
                path = repository_root / os.fsdecode(name)
                mode = path.lstat().st_mode
                digest.update(name)
                digest.update(f"\0{stat.S_IFMT(mode):o}:{mode & 0o111:o}\0".encode())
                if stat.S_ISLNK(mode):
                    digest.update(os.fsencode(os.readlink(path)))
                elif stat.S_ISREG(mode):
                    with path.open("rb") as handle:
                        for block in iter(lambda: handle.read(65536), b""):
                            digest.update(block)
                else:
                    return {**identity, "head": head.stdout.decode().strip(), "dirty": None,
                            "error": "An untracked special file cannot be fingerprinted"}
        return {**identity, "head": head.stdout.decode().strip(), "dirty": bool(status.stdout),
                "status": status.stdout.decode(errors="replace"), "worktree_sha256": digest.hexdigest()}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"head": None, "dirty": None, "error": str(exc)}


def _terminate_tree(process: subprocess.Popen[Any]) -> bool:
    """Stop descendants; return False when Windows has lost their leader.

    POSIX process groups survive their leader. Windows taskkill cannot establish
    descendant cleanup once the leader has exited; callers must retain that gap.
    """
    if os.name == "posix":
        # Reap a leader stopped by explicit teardown before signalling its group.
        # macOS may reject a signal to a group containing only an unreaped zombie.
        process.poll()
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=0.3)
        except subprocess.TimeoutExpired:
            pass
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=5)
        return True
    elif process.poll() is None:
        # Windows has no stdlib process-tree API; taskkill is the OS utility.
        result = subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], capture_output=True, timeout=10)
        process.wait(timeout=5)
        return result.returncode == 0
    return False


def _popen(argv: list[str], root: Path, output: Any) -> subprocess.Popen[Any]:
    return subprocess.Popen(argv, cwd=root, stdout=output, stderr=subprocess.STDOUT,
                            start_new_session=os.name == "posix")


def _supported(command: dict[str, Any]) -> bool:
    return "platforms" not in command or sys.platform in command["platforms"]


def _run_command(command: dict[str, Any], phase: str, root: Path, evidence: Path, number: int) -> dict[str, Any]:
    result = {"phase": phase, "name": command["name"], "argv": command["argv"],
              "timeout_seconds": command["timeout_seconds"]}
    if not _supported(command):
        return {**result, "status": "INCONCLUSIVE", "reason": f"Unsupported platform {sys.platform}", "duration_seconds": 0}
    log = evidence / f"{number:03d}-{phase}.log"
    started = time.monotonic()
    process = None
    try:
        with log.open("wb") as output:
            process = _popen(command["argv"], root, output)
            try:
                code = process.wait(timeout=command["timeout_seconds"])
                result.update(status="PASS" if code == 0 else "FAIL", returncode=code)
            except subprocess.TimeoutExpired:
                result.update(status="FAIL", reason="Command timed out", timed_out=True)
            finally:
                _terminate_tree(process)
    except OSError as exc:
        result.update(status="FAIL", reason=str(exc))
    result.update(duration_seconds=round(time.monotonic() - started, 4), log=log.name,
                  output=log.read_text(encoding="utf-8", errors="replace")[-16384:] if log.exists() else "")
    return result


def run_verification(root: str | Path, manifest: dict[str, Any], evidence_dir: str | Path) -> dict[str, Any]:
    """Execute explicit phases, preserve logs, always clean up, return a verdict.

    A launch command's timeout is the readiness budget. Health commands retry
    within that budget while the launch process is alive. Ordinary commands have
    individual timeouts; all cleanup commands are attempted even after a failure.
    """
    root = _root(root)
    validate_manifest(manifest)
    evidence = Path(evidence_dir).resolve()
    evidence.mkdir(parents=True, exist_ok=True)
    report_path = evidence / "report.json"
    if report_path.exists() or any(evidence.glob("[0-9][0-9][0-9]-*.log")):
        raise VerificationError("Evidence directory already contains a run; choose a new directory")
    source = _git_state(root)
    report: dict[str, Any] = {"version": 1, "project": manifest["project"], "platform": sys.platform,
                             "source": source, "commands": [], "ci_exceptions": manifest["ci_exceptions"]}
    started = time.monotonic()
    launch = None
    launch_output = None
    launch_result = None
    failed = False
    blocked = False
    incomplete = bool(manifest["ci_exceptions"]) or source.get("head") is None or source.get("dirty") is None

    def execute(command: dict[str, Any], phase: str) -> dict[str, Any]:
        result = _run_command(command, phase, root, evidence, len(report["commands"]) + 1)
        report["commands"].append(result)
        return result

    try:
        if manifest["launch"] is not None:
            command = manifest["launch"]
            launch_result = {"phase": "launch", "name": command["name"], "argv": command["argv"],
                             "timeout_seconds": command["timeout_seconds"]}
            report["commands"].append(launch_result)
            if not _supported(command):
                launch_result.update(status="INCONCLUSIVE", reason=f"Unsupported platform {sys.platform}")
                incomplete = True
                blocked = True  # Dependent proof cannot run without its service.
            else:
                launch_result["log"] = "000-launch.log"
                launch_output = (evidence / "000-launch.log").open("wb")
                launch = _popen(command["argv"], root, launch_output)
                launch_result.update(status="RUNNING", pid=launch.pid)
        for phase in ("health", "interaction", "checks"):
            if failed or blocked:
                break
            for command in manifest[phase]:
                deadline = started + manifest["launch"]["timeout_seconds"] if phase == "health" and launch else 0
                while True:
                    effective = command
                    if deadline:
                        effective = {**command, "timeout_seconds": min(command["timeout_seconds"], max(.001, deadline - time.monotonic()))}
                    result = execute(effective, phase)
                    if result["status"] != "FAIL" or not deadline or time.monotonic() >= deadline or launch.poll() is not None:
                        break
                    result["superseded_by_retry"] = True
                    time.sleep(min(0.1, max(0, deadline - time.monotonic())))
                failed = result["status"] == "FAIL"
                incomplete = incomplete or result["status"] == "INCONCLUSIVE"
                blocked = result["status"] == "INCONCLUSIVE" and phase in {"health", "interaction"}
                if launch and launch.poll() is not None:
                    launch_result.update(status="FAIL", returncode=launch.returncode, reason="Launch process exited before cleanup")
                    failed = True
                if failed or blocked:
                    break
    except (OSError, subprocess.SubprocessError, KeyboardInterrupt) as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
        if launch_result is not None:
            launch_result.update(status="FAIL", reason=str(exc))
        failed = True
    finally:
        # Check liveness before teardown: cleanup is allowed to stop the service.
        if launch is not None and launch.poll() is not None and launch_result["status"] == "RUNNING":
            launch_result.update(status="FAIL", returncode=launch.returncode, reason="Launch process exited before cleanup")
            failed = True
        for command in manifest["cleanup"]:
            try:
                result = execute(command, "cleanup")
                failed = failed or result["status"] == "FAIL"
                incomplete = incomplete or result["status"] == "INCONCLUSIVE"
            except (OSError, subprocess.SubprocessError, KeyboardInterrupt) as exc:
                report["commands"].append({"phase": "cleanup", "name": command["name"], "status": "FAIL", "reason": str(exc)})
                failed = True
        if launch is not None:
            try:
                confirmed = _terminate_tree(launch)
                launch_result["process_tree_cleanup_confirmed"] = confirmed
                if not confirmed:
                    incomplete = True
                    report.setdefault("limitations", []).append("Windows descendant cleanup could not be confirmed after the launch process exited")
                    if launch_result["status"] == "RUNNING":
                        launch_result.update(status="INCONCLUSIVE", reason=report["limitations"][-1])
                elif launch_result["status"] == "RUNNING":
                    launch_result["status"] = "PASS"
                launch_result["terminated_by_harness"] = confirmed
            except (OSError, subprocess.SubprocessError) as exc:
                launch_result.update(status="FAIL", reason=f"Process cleanup failed: {exc}")
                failed = True
        if launch_output is not None:
            launch_output.close()
        final_source = _git_state(root)
        source_changed = any(source.get(key) != final_source.get(key) for key in ("head", "worktree_sha256"))
        incomplete = incomplete or source_changed
        report.update(verdict="FAIL" if failed else "INCONCLUSIVE" if incomplete else "PASS",
                      duration_seconds=round(time.monotonic() - started, 4), final_source=final_source,
                      source_changed=source_changed)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("discover", "scaffold", "skill", "run"):
        command = subparsers.add_parser(name)
        command.add_argument("root", type=Path)
        if name in {"discover", "scaffold"}:
            command.add_argument("--output", type=Path)
        else:
            command.add_argument("--manifest", type=Path, required=True)
        if name == "skill":
            command.add_argument("--output", type=Path, required=True, help="Directory for project-verification/SKILL.md")
            command.add_argument("--force", action="store_true")
        if name == "run":
            command.add_argument("--evidence", type=Path, required=True, help="New evidence directory; existing runs are preserved")
    args = parser.parse_args(argv)
    try:
        if args.command in {"discover", "scaffold"}:
            result = discover(args.root) if args.command == "discover" else scaffold(args.root)
            output = json.dumps(result, indent=2) + "\n"
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                with args.output.open("x", encoding="utf-8") as handle:
                    handle.write(output)
            else:
                print(output, end="")
            return 0
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        if args.command == "skill":
            print(generate_skill(args.root, manifest, args.output, args.force))
            return 0
        report = run_verification(args.root, manifest, args.evidence)
        print(json.dumps({"verdict": report["verdict"], "evidence": str(args.evidence / "report.json")}))
        return {"PASS": 0, "FAIL": 1, "INCONCLUSIVE": 2}[report["verdict"]]
    except (VerificationError, OSError, json.JSONDecodeError) as exc:
        print(f"verification: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
