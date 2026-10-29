#!/usr/bin/env python3
"""Read-only evidence checks for delivery; this tool never merges or deletes.

Acceptance record: {"fingerprint": <fingerprint output>, "verdict": "PASS",
"reviewer": "identity", "evidence": ["link or artifact"],
"prerequisites": [{"name": "parent PR", "state": "MERGED"}]}.

Cleanup record: {"factory_created": true, "branch": "topic", "head_sha": "...",
"target_ref": "origin/main", "original_branch": "main", "default_branch": "main",
"protected_branches": [], "dependencies": []}. For a squash/rebase merge, add
"merged_pr": {"provenance": "GitHub API URL or saved response", "state": "MERGED",
"head_sha": "...", "merge_commit_sha": "...", "target_ref": "origin/main"}.
Dependency entries use the same name/state shape as prerequisites.
Cleanup targets must name a local or remote branch (for example main,
origin/main, or refs/remotes/origin/main); SHAs, tags, HEAD and revision
expressions cannot establish the identity of an intended integration branch.

Ownership, protection metadata, reviewer independence, and GitHub PR evidence are
caller-supplied declarations, not authenticated by this local helper. Obtain them
from fresh trusted records. The helper verifies the current Git facts and refuses
missing/ambiguous evidence. An ALLOW decision is an observation, not permission or
a guarantee against later races; recheck before any separately authorized action.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


class GuardError(Exception):
    """A fact required for a decision could not be established."""


def git(root, *args, check=True):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, env=env, timeout=20
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GuardError(f"Git fact unavailable: {type(exc).__name__}") from exc
    if check and result.returncode:
        raise GuardError(f"Git fact unavailable: {args[0]} exited {result.returncode}")
    return result


def output(root, *args):
    return git(root, *args).stdout.decode("utf-8", errors="strict").strip()


def commit(root, ref):
    return output(root, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}")


def fingerprint(root, base, head):
    """Identify the repository and the exact committed PR-style three-dot diff."""
    root = Path(output(root, "rev-parse", "--show-toplevel"))
    common = Path(output(root, "rev-parse", "--git-common-dir"))
    if not common.is_absolute():
        common = root / common
    origin = git(root, "remote", "get-url", "origin", check=False)
    base_sha, head_sha = commit(root, base), commit(root, head)
    merge_base = output(root, "merge-base", base_sha, head_sha)
    diff = git(
        root, "-c", "core.quotePath=true", "diff", "--no-color", "--no-ext-diff",
        "--no-textconv", "--no-renames", "--full-index", "--binary",
        "--src-prefix=a/", "--dst-prefix=b/", merge_base, head_sha, "--"
    ).stdout
    return {
        "repository": {"common_dir": str(common.resolve()),
                       "origin": origin.stdout.decode().strip() if origin.returncode == 0 else None},
        "base_ref": base, "base_sha": base_sha, "head_ref": head, "head_sha": head_sha,
        "merge_base": merge_base, "diff_sha256": hashlib.sha256(diff).hexdigest(),
    }


def named_merged(items, label, reasons):
    if not isinstance(items, list):
        reasons.append(f"{label} must be an explicit list")
        return
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not item["name"].strip():
            reasons.append(f"{label} contains an unnamed dependency")
        elif item.get("state") != "MERGED":
            reasons.append(f"{label} has an unresolved dependency: {item['name']}")


def decision(reasons, **facts):
    return {"decision": "BLOCK" if reasons else "ALLOW", "reasons": reasons, **facts}


def acceptance(root, record, base, head):
    reasons = []
    current = fingerprint(root, base, head)
    previous = record.get("fingerprint")
    if previous != current:
        reasons.append("Acceptance fingerprint does not match the current repository, head, base, or patch")
    if record.get("verdict") != "PASS":
        reasons.append("Independent acceptance verdict must be PASS")
    if not isinstance(record.get("reviewer"), str) or not record["reviewer"].strip():
        reasons.append("Acceptance reviewer is missing")
    evidence = record.get("evidence")
    if not isinstance(evidence, list) or not evidence or not all(isinstance(x, str) and x.strip() for x in evidence):
        reasons.append("Acceptance evidence must contain nonempty artifact references")
    named_merged(record.get("prerequisites", []), "prerequisites", reasons)
    if git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all").stdout:
        reasons.append("Checkout has uncommitted or untracked work")
    return decision(reasons, fingerprint=current)


def worktrees(root):
    result = git(root, "worktree", "list", "--porcelain", "-z").stdout
    trees = []
    for chunk in result.split(b"\0\0"):
        values = {}
        for entry in chunk.split(b"\0"):
            if not entry:
                continue
            key, _, value = entry.partition(b" ")
            values[key.decode()] = os.fsdecode(value)
        if values:
            trees.append(values)
    return trees


def is_ancestor(root, older, newer):
    result = git(root, "merge-base", "--is-ancestor", older, newer, check=False)
    if result.returncode not in (0, 1):
        raise GuardError("Cannot establish commit ancestry")
    return result.returncode == 0


def cleanup(root, branch, record, target):
    reasons = []
    if git(root, "check-ref-format", "refs/heads/" + branch, check=False).returncode:
        raise GuardError("Invalid branch name")
    head_sha, target_sha = commit(root, "refs/heads/" + branch), commit(root, target)
    if record.get("factory_created") is not True or record.get("branch") != branch:
        reasons.append("Exact branch has no positive factory ownership record")
    if record.get("head_sha") != head_sha:
        reasons.append("Local branch tip differs from the recorded factory-created tip")
    if record.get("target_ref") != target:
        reasons.append("Integration target differs from the recorded target")
    preserved = []
    for field in ("original_branch", "default_branch"):
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            reasons.append(f"Missing {field} preservation metadata")
        else:
            preserved.append(value)
    protected = record.get("protected_branches")
    if not isinstance(protected, list) or not all(isinstance(x, str) and x.strip() for x in protected):
        reasons.append("Missing explicit protected branch inventory")
    else:
        preserved.extend(protected)
    if branch in preserved:
        reasons.append("Branch is original, default, or explicitly protected")
    named_merged(record.get("dependencies"), "dependencies", reasons)
    remotes = output(root, "remote").splitlines()
    target_name = output(root, "rev-parse", "--symbolic-full-name", "--verify", "--end-of-options", target)
    symbolic = git(root, "symbolic-ref", "--quiet", target_name, check=False)
    if symbolic.returncode == 0:
        target_name = symbolic.stdout.decode().strip()
    spellings = set()
    if target_name.startswith("refs/heads/"):
        spellings = {target_name, target_name.removeprefix("refs/heads/")}
    elif target_name.startswith("refs/remotes/"):
        spellings = {target_name, target_name.removeprefix("refs/remotes/")}
        if not any(target_name.startswith("refs/remotes/" + remote + "/") for remote in remotes):
            reasons.append("Remote integration branch has no configured remote identity")
    if target not in spellings:
        reasons.append("Integration target must name a canonical local or remote branch, not a SHA, tag, HEAD, or revision expression")
    topic_names = {"refs/heads/" + branch}
    topic_names.update("refs/remotes/" + remote + "/" + branch for remote in remotes)
    if target_name in topic_names:
        reasons.append("A topic branch cannot prove integration into itself")
    trees = worktrees(root)
    if not trees:
        reasons.append("Worktree inventory is empty or unavailable")
    for tree in trees:
        path = tree.get("worktree")
        if tree.get("branch") == "refs/heads/" + branch:
            reasons.append("Branch is checked out in a worktree: " + str(path))
        if not path or not Path(path).is_dir():
            reasons.append("A worktree cannot be inspected: " + str(path))
            continue
        state = git(path, "status", "--porcelain=v1", "-z", "--untracked-files=all", check=False)
        if state.returncode:
            reasons.append("Cannot establish clean worktree state: " + path)
        elif state.stdout:
            reasons.append("Worktree contains uncommitted or untracked work: " + path)
    integration = "ancestry"
    if not is_ancestor(root, head_sha, target_sha):
        integration = "caller-supplied merged PR proof"
        proof = record.get("merged_pr")
        valid = isinstance(proof, dict)
        if valid:
            valid = (
                proof.get("state") == "MERGED" and proof.get("head_sha") == head_sha
                and proof.get("target_ref") == target
                and isinstance(proof.get("provenance"), str) and bool(proof["provenance"].strip())
                and isinstance(proof.get("merge_commit_sha"), str)
            )
        if valid:
            try:
                merged = commit(root, proof["merge_commit_sha"])
                valid = merged == proof["merge_commit_sha"] and is_ancestor(root, merged, target_sha)
            except GuardError:
                valid = False
        if not valid:
            reasons.append("Branch is not integrated by ancestry or authoritative exact-head merged PR evidence")
    remote_tip = None
    if "origin" in remotes:
        remote = git(root, "ls-remote", "--exit-code", "origin", "refs/heads/" + branch, check=False)
        if remote.returncode == 0:
            lines = remote.stdout.decode().strip().splitlines()
            if len(lines) != 1 or len(lines[0].split()) != 2:
                reasons.append("Origin branch response is ambiguous")
            else:
                remote_tip = lines[0].split()[0]
                if remote_tip != head_sha:
                    reasons.append("Origin branch tip differs from the recorded topic tip")
        elif remote.returncode != 2:
            reasons.append("Origin branch could not be verified; remote state is inconclusive")
    elif remotes:
        reasons.append("Origin is missing while other remotes exist; remote identity is ambiguous")
    return decision(reasons, branch=branch, head_sha=head_sha, target_ref=target,
                    target_sha=target_sha, remote_tip=remote_tip, integration=integration,
                    proof_authentication="Caller authenticates ownership, protection metadata, and PR evidence")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("fingerprint", "acceptance", "cleanup"):
        command = sub.add_parser(name)
        command.add_argument("root", type=Path)
        if name in ("fingerprint", "acceptance"):
            command.add_argument("--base", required=True)
            command.add_argument("--head", required=True)
        if name in ("acceptance", "cleanup"):
            command.add_argument("--record", type=Path, required=True)
        if name == "cleanup":
            command.add_argument("--branch", required=True)
            command.add_argument("--target", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "fingerprint":
            result = fingerprint(args.root, args.base, args.head)
        else:
            record = json.loads(args.record.read_text())
            if not isinstance(record, dict):
                raise GuardError("Evidence record must be a JSON object")
            result = (acceptance(args.root, record, args.base, args.head) if args.command == "acceptance"
                      else cleanup(args.root, args.branch, record, args.target))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1 if result.get("decision") == "BLOCK" else 0
    except (GuardError, OSError, ValueError) as exc:
        print(json.dumps(decision([str(exc)]), indent=2, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
