"""Real Git scenarios in disposable checkouts and a local bare remote."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "plugins/factory/scripts/delivery_guard.py"
SPEC = importlib.util.spec_from_file_location("delivery_guard", SCRIPT)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class DeliveryGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.remote = self.directory / "remote.git"
        self.root = self.directory / "checkout"
        self.run_git(self.directory, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.run_git(self.directory, "clone", str(self.remote), str(self.root))
        self.identity(self.root)
        self.write_commit("base.txt", "base", "initial")
        self.run_git(self.root, "push", "-u", "origin", "main")
        self.run_git(self.root, "switch", "-c", "factory/topic")
        self.write_commit("feature.txt", "feature", "feature")
        self.head = guard.commit(self.root, "factory/topic")
        self.run_git(self.root, "push", "-u", "origin", "factory/topic")
        self.run_git(self.root, "switch", "main")

    def run_git(self, root, *args):
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def identity(self, root):
        self.run_git(root, "config", "user.name", "Factory Test")
        self.run_git(root, "config", "user.email", "factory@example.invalid")
        self.run_git(root, "config", "commit.gpgsign", "false")

    def write_commit(self, file, text, message, root=None):
        root = root or self.root
        (root / file).write_text(text)
        self.run_git(root, "add", "--", file)
        self.run_git(root, "commit", "-m", message)

    def acceptance_record(self):
        return {"fingerprint": guard.fingerprint(self.root, "main", "factory/topic"),
                "verdict": "PASS", "reviewer": "independent-test-reviewer",
                "evidence": ["test-output.json"], "prerequisites": []}

    def cleanup_record(self):
        return {"factory_created": True, "branch": "factory/topic", "head_sha": self.head,
                "target_ref": "origin/main", "original_branch": "main", "default_branch": "main",
                "protected_branches": [], "dependencies": []}

    def cleanup_decision(self, record=None, target="origin/main"):
        return guard.cleanup(self.root, "factory/topic", record or self.cleanup_record(), target)

    def merge_topic(self, squash=False):
        self.run_git(self.root, "merge", "--squash" if squash else "--ff-only", "factory/topic")
        if squash:
            self.run_git(self.root, "commit", "-m", "squash feature")
        self.run_git(self.root, "push", "origin", "main")
        return guard.commit(self.root, "main")

    def assert_block(self, result, fragment=None):
        self.assertEqual(result["decision"], "BLOCK", result)
        if fragment:
            self.assertTrue(any(fragment in reason for reason in result["reasons"]), result)

    def test_current_acceptance_allows_exact_committed_patch(self):
        record = self.acceptance_record()
        result = guard.acceptance(self.root, record, "main", "factory/topic")
        self.assertEqual(result["decision"], "ALLOW", result)
        self.assertEqual(len(result["fingerprint"]["diff_sha256"]), 64)

    def test_acceptance_rejects_advanced_head(self):
        record = self.acceptance_record()
        self.run_git(self.root, "switch", "factory/topic")
        self.write_commit("extra.txt", "useful new work", "additional change")
        self.run_git(self.root, "switch", "main")
        self.assert_block(guard.acceptance(self.root, record, "main", "factory/topic"), "fingerprint")

    def test_acceptance_rejects_advanced_base_even_when_patch_is_unchanged(self):
        record = self.acceptance_record()
        self.write_commit("unrelated.txt", "another change", "base advanced")
        current = guard.fingerprint(self.root, "main", "factory/topic")
        self.assertEqual(current["diff_sha256"], record["fingerprint"]["diff_sha256"])
        self.assert_block(guard.acceptance(self.root, record, "main", "factory/topic"), "fingerprint")

    def test_acceptance_rejects_retarget_to_equal_sha_alias(self):
        record = self.acceptance_record()
        self.assert_block(guard.acceptance(self.root, record, "origin/main", "factory/topic"), "fingerprint")

    def test_acceptance_requires_verdict_reviewer_and_evidence(self):
        for key, value in (("verdict", "INCONCLUSIVE"), ("reviewer", ""), ("evidence", []), ("evidence", [""])):
            with self.subTest(key=key, value=value):
                record = self.acceptance_record()
                record[key] = value
                self.assert_block(guard.acceptance(self.root, record, "main", "factory/topic"))

    def test_acceptance_rejects_open_prerequisite(self):
        record = self.acceptance_record()
        record["prerequisites"] = [{"name": "parent PR", "state": "OPEN"}]
        self.assert_block(guard.acceptance(self.root, record, "main", "factory/topic"), "unresolved")

    def test_acceptance_rejects_dirty_checkout(self):
        record = self.acceptance_record()
        (self.root / "untracked.txt").write_text("keep me")
        self.assert_block(guard.acceptance(self.root, record, "main", "factory/topic"), "untracked")

    def test_clean_merged_topic_is_eligible_without_mutating_git(self):
        self.merge_topic()
        before = self.run_git(self.root, "show-ref")
        result = self.cleanup_decision()
        self.assertEqual(result["decision"], "ALLOW", result)
        self.assertEqual(before, self.run_git(self.root, "show-ref"))
        self.assertEqual(self.run_git(self.root, "status", "--porcelain"), "")
        self.assertTrue((self.root / "feature.txt").exists())

    def test_unmerged_topic_is_preserved(self):
        self.assert_block(self.cleanup_decision(), "not integrated")

    def test_dirty_or_untracked_original_checkout_is_preserved(self):
        self.merge_topic()
        for filename in ("base.txt", "untracked.txt"):
            with self.subTest(filename=filename):
                path = self.root / filename
                previous = path.read_text() if path.exists() else None
                path.write_text("valuable work")
                self.assert_block(self.cleanup_decision(), "uncommitted or untracked")
                self.assertEqual(path.read_text(), "valuable work")
                if previous is None:
                    path.unlink()
                else:
                    path.write_text(previous)

    def test_active_topic_worktree_blocks_cleanup(self):
        self.merge_topic()
        tree = self.directory / "active-worktree"
        self.run_git(self.root, "worktree", "add", str(tree), "factory/topic")
        self.assert_block(self.cleanup_decision(), "checked out in a worktree")
        self.assertTrue(tree.is_dir())

    def test_dirty_other_worktree_blocks_cleanup(self):
        self.merge_topic()
        tree = self.directory / "other-worktree"
        self.run_git(self.root, "worktree", "add", "-b", "other", str(tree), "main")
        (tree / "keep.txt").write_text("valuable")
        self.assert_block(self.cleanup_decision(), "uncommitted or untracked")

    def test_new_useful_topic_commit_is_preserved(self):
        self.merge_topic()
        self.run_git(self.root, "switch", "factory/topic")
        self.write_commit("later.txt", "valuable", "post-merge commit")
        self.run_git(self.root, "switch", "main")
        self.assert_block(self.cleanup_decision(), "Local branch tip differs")

    def test_unknown_ownership_original_default_and_protected_branches_are_preserved(self):
        self.merge_topic()
        for key, value in (("factory_created", False), ("original_branch", "factory/topic"),
                           ("default_branch", "factory/topic"), ("protected_branches", ["factory/topic"]),
                           ("protected_branches", None), ("original_branch", None), ("default_branch", None)):
            with self.subTest(key=key, value=value):
                record = self.cleanup_record()
                record[key] = value
                self.assert_block(self.cleanup_decision(record))

    def test_open_or_unknown_dependencies_block_cleanup(self):
        self.merge_topic()
        for dependencies in (None, [{"name": "child PR", "state": "OPEN"}], [{}]):
            record = self.cleanup_record()
            record["dependencies"] = dependencies
            self.assert_block(self.cleanup_decision(record))

    def test_squash_merge_requires_attributed_exact_head_evidence(self):
        merged = self.merge_topic(squash=True)
        self.assertFalse(guard.is_ancestor(self.root, self.head, merged))
        self.assert_block(self.cleanup_decision(), "not integrated")
        record = self.cleanup_record()
        record["merged_pr"] = {"provenance": "saved trusted GitHub response for PR 1", "state": "MERGED",
                               "head_sha": self.head, "merge_commit_sha": merged, "target_ref": "origin/main"}
        self.assertEqual(self.cleanup_decision(record)["decision"], "ALLOW")
        for key, value in (("provenance", ""), ("head_sha", "0" * 40), ("merge_commit_sha", "0" * 40),
                           ("state", "OPEN"), ("target_ref", "origin/other")):
            bad = copy.deepcopy(record)
            bad["merged_pr"][key] = value
            self.assert_block(self.cleanup_decision(bad), "not integrated")

    def test_remote_topic_advance_blocks_even_without_fetch(self):
        self.merge_topic()
        other = self.directory / "second-checkout"
        self.run_git(self.directory, "clone", str(self.remote), str(other))
        self.identity(other)
        self.run_git(other, "switch", "factory/topic")
        self.write_commit("remote-only.txt", "valuable", "remote advanced", root=other)
        self.run_git(other, "push", "origin", "factory/topic")
        self.assert_block(self.cleanup_decision(), "Origin branch tip differs")

    def test_missing_remote_branch_is_allowed_but_unreachable_remote_blocks(self):
        self.merge_topic()
        self.run_git(self.root, "push", "origin", "--delete", "factory/topic")
        self.assertEqual(self.cleanup_decision()["decision"], "ALLOW")
        self.run_git(self.root, "remote", "set-url", "origin", str(self.directory / "missing.git"))
        self.assert_block(self.cleanup_decision(), "inconclusive")

    def test_integration_target_must_match_record_and_cannot_be_topic(self):
        self.merge_topic()
        self.assert_block(self.cleanup_decision(target="main"), "target differs")
        for target in ("factory/topic", "refs/heads/factory/topic", "origin/factory/topic",
                       "refs/remotes/origin/factory/topic"):
            with self.subTest(target=target):
                record = self.cleanup_record()
                record["target_ref"] = target
                self.assert_block(self.cleanup_decision(record, target), "into itself")

    def test_sha_tag_and_revision_expression_cannot_self_prove_unmerged_topic(self):
        self.run_git(self.root, "tag", "topic-proof", "factory/topic")
        for target in (self.head, "topic-proof", "refs/tags/topic-proof", "factory/topic^0",
                       "factory/topic~0", "refs/heads/factory/topic^{commit}"):
            with self.subTest(target=target):
                record = self.cleanup_record()
                record["target_ref"] = target
                self.assert_block(self.cleanup_decision(record, target), "must name a canonical")

    def test_only_named_canonical_integration_branch_aliases_are_accepted(self):
        self.merge_topic()
        for target in ("main", "refs/heads/main", "origin/main", "refs/remotes/origin/main"):
            with self.subTest(target=target):
                record = self.cleanup_record()
                record["target_ref"] = target
                self.assertEqual(self.cleanup_decision(record, target)["decision"], "ALLOW")
        for target in ("HEAD", "main^0", "origin/main~0"):
            with self.subTest(target=target):
                record = self.cleanup_record()
                record["target_ref"] = target
                self.assert_block(self.cleanup_decision(record, target), "must name a canonical")

    def test_cli_blocks_malformed_records_and_has_nonzero_status(self):
        record_path = self.directory / "record.json"
        record_path.write_text("[]")
        result = subprocess.run([sys.executable, str(SCRIPT), "acceptance", str(self.root),
                                 "--record", str(record_path), "--base", "main", "--head", "factory/topic"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["decision"], "BLOCK")


if __name__ == "__main__":
    unittest.main()
