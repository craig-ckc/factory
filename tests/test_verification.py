"""Behavioral checks for project verification and mandatory teardown."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "plugins/factory/scripts/verification.py"
SPEC = importlib.util.spec_from_file_location("factory_verification", SCRIPT)
verification = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verification)


def command(name, code="pass", timeout=3, **extra):
    return {"name": name, "argv": [sys.executable, "-c", code], "timeout_seconds": timeout, **extra}


def manifest():
    return {"version": 1, "project": "example", "launch": None,
            "health": [command("health")], "interaction": [command("flow")],
            "checks": [command("local-ci")], "cleanup": [command("cleanup")], "ci_exceptions": []}


class VerificationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.evidence = self.root / "evidence"

    def run_manifest(self, data):
        with patch.object(verification, "_git_state", return_value={"head": "a" * 40, "dirty": False}):
            return verification.run_verification(self.root, data, self.evidence)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def init_git(self):
        self.git("init", "--quiet")
        (self.root / "tracked.txt").write_text("base\n")
        self.git("add", "tracked.txt")
        self.git("-c", "user.name=Verification Test", "-c", "user.email=verification@example.invalid", "commit", "--quiet", "-m", "base")

    def test_git_identity_uses_repository_root_for_nested_project(self):
        self.init_git()
        project = self.root / "nested"
        project.mkdir()
        before = verification._git_state(project)
        (self.root / "untracked").write_text("outside nested project\n")
        after = verification._git_state(project)
        self.assertEqual(after["repository_root"], str(self.root.resolve()))
        self.assertEqual(after["project_root"], str(project))
        self.assertEqual(after["mode"], "worktree")
        self.assertNotEqual(before["worktree_sha256"], after["worktree_sha256"])

    def test_git_identity_does_not_execute_diff_drivers(self):
        self.init_git()
        (self.root / ".gitattributes").write_text("*.txt diff=unsafe\n")
        driver = sys.executable + ' -c "from pathlib import Path; Path(\'unexpected\').touch()"'
        self.git("config", "diff.unsafe.textconv", driver)
        self.git("config", "diff.external", driver)
        before = verification._git_state(self.root)
        (self.root / "tracked.txt").write_text("changed\n")
        after = verification._git_state(self.root)
        self.assertFalse((self.root / "unexpected").exists())
        self.assertNotEqual(before["worktree_sha256"], after["worktree_sha256"])

    @unittest.skipUnless(os.name == "posix", "POSIX executable modes")
    def test_git_identity_records_modes_even_when_git_ignores_filemode(self):
        self.init_git()
        self.git("config", "core.filemode", "false")
        tracked = self.root / "tracked.txt"
        untracked = self.root / "untracked"
        untracked.write_text("same contents")
        tracked.chmod(0o644)
        untracked.chmod(0o644)
        before = verification._git_state(self.root)
        tracked.chmod(0o755)
        tracked_mode = verification._git_state(self.root)
        untracked.chmod(0o755)
        untracked_mode = verification._git_state(self.root)
        self.assertNotEqual(before["worktree_sha256"], tracked_mode["worktree_sha256"])
        self.assertNotEqual(tracked_mode["worktree_sha256"], untracked_mode["worktree_sha256"])

    def test_discovery_inventories_without_executing(self):
        (self.root / "package.json").write_text(json.dumps({"scripts": {"test": "touch SHOULD_NOT_EXIST"}}))
        workflows = self.root / ".github/workflows"
        workflows.mkdir(parents=True)
        (workflows / "ci.yml").write_text("jobs:\n  test:\n    runs-on: windows-latest\n    steps:\n      - run: npm test\n")
        result = verification.discover(self.root)
        self.assertTrue(result["candidate_only"])
        self.assertEqual(result["packages"][0]["scripts"], {"test": "touch SHOULD_NOT_EXIST"})
        self.assertEqual(len(result["workflows"]), 1)
        self.assertFalse((self.root / "SHOULD_NOT_EXIST").exists())

    def test_incomplete_scaffold_is_rejected_before_commands(self):
        data = verification.scaffold(self.root)
        with self.assertRaises(verification.VerificationError):
            self.run_manifest(data)
        self.assertFalse(self.evidence.exists())

    def test_success_records_each_phase_and_output(self):
        data = manifest()
        data["interaction"] = [command("flow", "print('observed result')")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual([item["phase"] for item in report["commands"]], ["health", "interaction", "checks", "cleanup"])
        self.assertIn("observed result", report["commands"][1]["output"])
        saved = json.loads((self.evidence / "report.json").read_text())
        self.assertEqual(saved["source"]["head"], "a" * 40)
        self.assertEqual(saved["commands"][1]["status"], "PASS")

    def test_failure_stops_proof_but_always_runs_all_cleanup(self):
        data = manifest()
        data["interaction"] = [command("failed", "raise SystemExit(7)")]
        data["cleanup"] = [command("failed-cleanup", "raise SystemExit(1)"),
                           command("sentinel", "from pathlib import Path; Path('cleaned').write_text('yes')")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "FAIL")
        self.assertTrue((self.root / "cleaned").exists())
        self.assertNotIn("checks", [item["phase"] for item in report["commands"]])
        self.assertEqual(report["commands"][1]["returncode"], 7)

    def test_command_timeout_preserves_evidence_and_cleans_up(self):
        data = manifest()
        data["interaction"] = [command("hung", "import time; print('before timeout', flush=True); time.sleep(20)", .15)]
        data["cleanup"] = [command("sentinel", "from pathlib import Path; Path('cleaned').touch()")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "FAIL")
        self.assertTrue(report["commands"][1]["timed_out"])
        self.assertIn("before timeout", report["commands"][1]["output"])
        self.assertTrue((self.root / "cleaned").exists())

    @unittest.skipUnless(os.name == "posix", "POSIX process group regression")
    def test_launch_and_descendant_are_stopped(self):
        data = manifest()
        child = "from pathlib import Path; import time\nwhile True:\n Path('heartbeat').write_text(str(time.time_ns()))\n time.sleep(.03)"
        service = "import subprocess, sys, time; subprocess.Popen([sys.executable, '-c', " + repr(child) + "]); time.sleep(20)"
        data["launch"] = command("service", service, 2)
        data["health"] = [command("ready", "from pathlib import Path; assert Path('heartbeat').exists()")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "PASS")
        previous = (self.root / "heartbeat").read_text()
        time.sleep(.15)
        self.assertEqual((self.root / "heartbeat").read_text(), previous)
        self.assertTrue(report["commands"][0]["terminated_by_harness"])

    def test_launch_failure_still_runs_cleanup(self):
        data = manifest()
        data["launch"] = {"name": "missing", "argv": [str(self.root / "missing")], "timeout_seconds": 1}
        data["cleanup"] = [command("sentinel", "from pathlib import Path; Path('cleaned').touch()")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "FAIL")
        self.assertTrue((self.root / "cleaned").exists())

    @unittest.skipUnless(os.name == "posix", "POSIX process group regression")
    def test_readiness_timeout_stops_launch_descendants_and_runs_cleanup(self):
        data = manifest()
        child = "from pathlib import Path; import time\nwhile True:\n Path('heartbeat').write_text(str(time.time_ns()))\n time.sleep(.03)"
        service = "import subprocess, sys, time; subprocess.Popen([sys.executable, '-c', " + repr(child) + "]); time.sleep(20)"
        data["launch"] = command("service", service, .3)
        data["health"] = [command("never-ready", "import time; time.sleep(20)", 3)]
        data["cleanup"] = [command("sentinel", "from pathlib import Path; Path('cleaned').touch()")]
        started = time.monotonic()
        report = self.run_manifest(data)
        self.assertLess(time.monotonic() - started, 2)
        self.assertEqual(report["verdict"], "FAIL")
        self.assertTrue((self.root / "cleaned").exists())
        previous = (self.root / "heartbeat").read_text()
        time.sleep(.15)
        self.assertEqual((self.root / "heartbeat").read_text(), previous)

    @unittest.skipUnless(os.name == "posix", "POSIX service lifecycle regression")
    def test_explicit_cleanup_may_stop_launched_service(self):
        data = manifest()
        data["launch"] = command("service", "from pathlib import Path; import os, time; Path('service.pid').write_text(str(os.getpid())); time.sleep(20)", 2)
        data["health"] = [command("ready", "from pathlib import Path; assert Path('service.pid').exists()")]
        data["cleanup"] = [command("stop-service", "from pathlib import Path; import os, signal; os.kill(int(Path('service.pid').read_text()), signal.SIGTERM)")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["commands"][0]["status"], "PASS")
        self.assertTrue(report["commands"][0]["process_tree_cleanup_confirmed"])

    @unittest.skipUnless(os.name == "posix", "Use POSIX process to simulate cleanup confirmation gap")
    def test_unconfirmed_launch_descendant_cleanup_is_inconclusive(self):
        data = manifest()
        data["launch"] = command("service", "from pathlib import Path; import time; Path('ready').touch(); time.sleep(20)", 2)
        data["health"] = [command("ready", "from pathlib import Path; assert Path('ready').exists()")]
        terminate = verification._terminate_tree

        def unconfirmed_for_launch(process):
            confirmed = terminate(process)
            return False if process.args[2] == data["launch"]["argv"][2] else confirmed

        with patch.object(verification, "_terminate_tree", side_effect=unconfirmed_for_launch):
            report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "INCONCLUSIVE")
        self.assertFalse(report["commands"][0]["process_tree_cleanup_confirmed"])
        self.assertTrue(report["limitations"])

    def test_platform_and_ci_exceptions_are_not_passes(self):
        data = manifest()
        other_platform = next(item for item in verification.PLATFORMS if item != sys.platform)
        data["checks"][0]["platforms"] = [other_platform]
        data["ci_exceptions"] = [{"job": "hosted-deploy", "reason": "Requires hosted identity"}]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "INCONCLUSIVE")
        self.assertEqual(report["commands"][2]["status"], "INCONCLUSIVE")

    def test_unsupported_health_blocks_dependent_interaction(self):
        data = manifest()
        other_platform = next(item for item in verification.PLATFORMS if item != sys.platform)
        data["health"][0]["platforms"] = [other_platform]
        data["interaction"] = [command("sentinel", "from pathlib import Path; Path('interacted').touch()")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "INCONCLUSIVE")
        self.assertFalse((self.root / "interacted").exists())
        self.assertEqual(report["commands"][-1]["phase"], "cleanup")

    def test_cleanup_failure_outranks_unsupported_launch(self):
        data = manifest()
        other_platform = next(item for item in verification.PLATFORMS if item != sys.platform)
        data["launch"] = command("unsupported", platforms=[other_platform])
        data["cleanup"] = [command("failed-cleanup", "raise SystemExit(1)")]
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "FAIL")

    def test_source_change_during_run_is_inconclusive(self):
        with patch.object(verification, "_git_state", side_effect=[
                {"head": "a" * 40, "dirty": False, "worktree_sha256": "before"},
                {"head": "a" * 40, "dirty": True, "worktree_sha256": "after"}]):
            report = verification.run_verification(self.root, manifest(), self.evidence)
        self.assertEqual(report["verdict"], "INCONCLUSIVE")
        self.assertTrue(report["source_changed"])

    def test_argv_is_not_interpreted_by_a_shell(self):
        data = manifest()
        data["interaction"] = {"not": "a-list"}
        with self.assertRaises(verification.VerificationError):
            self.run_manifest(data)
        data["interaction"] = [command("literal", "import sys; print(sys.argv[1])")]
        data["interaction"][0]["argv"].append("$(touch injected); touch injected")
        report = self.run_manifest(data)
        self.assertEqual(report["verdict"], "PASS")
        self.assertFalse((self.root / "injected").exists())

    def test_absent_git_identity_is_inconclusive(self):
        report = verification.run_verification(self.root, manifest(), self.evidence)
        self.assertEqual(report["verdict"], "INCONCLUSIVE")
        self.assertIsNone(report["source"]["head"])

    def test_malformed_commands_are_rejected_before_execution(self):
        for mutate in (lambda d: d["checks"].clear(),
                       lambda d: d["health"][0].update(timeout_seconds=True),
                       lambda d: d["interaction"][0].update(argv="echo wrong"),
                       lambda d: d["cleanup"][0].update(timeout_seconds=float("inf"))):
            with self.subTest(mutate=mutate):
                data = manifest()
                mutate(data)
                with self.assertRaises(verification.VerificationError):
                    self.run_manifest(data)
        self.assertFalse(self.evidence.exists())

    def test_skill_is_self_contained_and_overwrite_requires_force(self):
        data = manifest()
        for phase in verification.PHASES:
            data[phase][0]["argv"][0] = "python3"
        output = self.root / ".agents/skills/project-verification"
        path = verification.generate_skill(self.root, data, output)
        text = path.read_text()
        self.assertTrue(text.startswith("---\nname: project-verification\n"))
        contract = json.loads(text.split("```json\n", 1)[1].split("```", 1)[0])
        self.assertEqual(contract, data)
        self.assertNotIn(str(self.root), text)
        with self.assertRaises(verification.VerificationError):
            verification.generate_skill(self.root, data, output)
        verification.generate_skill(self.root, data, output, force=True)

    def test_evidence_is_not_overwritten(self):
        self.run_manifest(manifest())
        original = (self.evidence / "report.json").read_bytes()
        with self.assertRaises(verification.VerificationError):
            self.run_manifest(manifest())
        self.assertEqual((self.evidence / "report.json").read_bytes(), original)

    def test_cli_requires_evidence_and_reports_nonpass_exit(self):
        contract = self.root / "verification.json"
        contract.write_text(json.dumps(manifest()))
        missing = subprocess.run([sys.executable, str(SCRIPT), "run", str(self.root), "--manifest", str(contract)], capture_output=True)
        self.assertNotEqual(missing.returncode, 0)
        result = subprocess.run([sys.executable, str(SCRIPT), "run", str(self.root), "--manifest", str(contract), "--evidence", str(self.evidence)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["verdict"], "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()
