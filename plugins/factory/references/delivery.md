# Revision acceptance and safe delivery

Use with GitHub Workflow and Release for integration, interrupted runs, stacked PRs, or branch cleanup. Honor the user's authorization and repository policy; a helper result does not grant merge/delete permission.

## Checkpoint and resume

Keep a compact record in the existing issue/PR or established local record:

- Repository identity, original checkout path, starting branch/upstream/SHA, and pre-existing dirty/untracked work.
- Factory-created topic branches/worktrees and their exact expected tips; never infer ownership from a name.
- Target branch tip, PR head, merge-base, patch identity, dependency PRs, required check runs, and independent reviewer/verdict/evidence.
- Merge/deployment result, local synchronization, cleanup decisions, unresolved blockers, and next action.

On resume, refresh Git/GitHub state and compare it with the checkpoint before acting. Do not replay stale next steps. Distinguish observed state from planned actions.

## Bind acceptance to content

```sh
python3 plugins/factory/scripts/delivery_guard.py fingerprint /path/to/repo --base origin/main --head topic
python3 plugins/factory/scripts/delivery_guard.py acceptance /path/to/repo --record acceptance.json --base origin/main --head topic
```

An acceptance record holds `fingerprint` (the complete emitted object), `verdict: "PASS"`, `reviewer`, nonempty `evidence`, and optional `prerequisites` with name/state records. The fingerprint binds repository, target ref and tip, head ref and SHA, merge-base, and binary diff digest. Record the PR URL alongside it in the durable issue/PR record. Obtain actual independent review; do not fill PASS from the author to satisfy the guard. Changed head, retargeting, patch or target tip invalidates this receipt. Refresh review of affected code and integration checks as appropriate; unchanged unaffected review reasoning can remain useful evidence.

Inventory stacked dependencies before merge. Merge parents first; after retarget/rebase, refresh the child's actual patch identity, independent acceptance and required checks. Never treat an old stacked approval as acceptance of its rewritten patch. Use an expected-head merge operation and inspect the resulting merge revision.

## Synchronize and clean safely

Return to the recorded original checkout/branch. Fetch the integrated target, then fast-forward only when the original work is clean and the ancestry permits it. Verify the integrated files and SHA locally. Preserve dirty or divergent work and report the precise blocker instead of resetting, stashing without consent, or manufacturing a clean checkout.

```sh
python3 plugins/factory/scripts/delivery_guard.py cleanup /path/to/repo --branch topic --record cleanup.json --target origin/main
```

The cleanup record requires positive `factory_created`, `branch`, exact `head_sha`, `original_branch`, `default_branch`, `protected_branches`, `dependencies`, and `target_ref`. Refresh protection metadata, active worktrees and dependent PRs from their actual sources immediately before cleanup. Unknown metadata or failed queries is a blocker. The helper is read-only; it checks the supplied metadata against live Git refs/worktrees/status. It cannot authenticate caller-supplied GitHub metadata or eliminate races after its snapshot.

Normal integration requires source-head ancestry in the intended target. For squash integration, provide authoritative merged-PR evidence for the exact head and target, plus a merge commit reachable from that target. `merged_pr` contains `provenance`, `state: "MERGED"`, `head_sha`, `merge_commit_sha`, and `target_ref`. If a rebase strategy does not provide an authoritative mapping to the integrated patch, retain the branch. A patch-id resemblance alone does not authorize deletion. Keep the source if it advanced after merge, contains useful commits, is dirty, is in use by a worktree, has open dependencies, has uncertain ownership, or is original/default/protected.

An ALLOW is a fresh precondition snapshot, not deletion authorization or a lasting guarantee. For remote deletion, compare the live expected tip and use an explicit expected-SHA lease; on mismatch, stop and refresh. For local deletion, recheck the tip immediately and use safe Git deletion when ancestry permits. Do not force-delete squash/rebase source branches just to satisfy cleanup: preserve them when safe integration proof or an atomic operation is unavailable. Use the app lifecycle tools for app-managed worktrees.

After release, verify the delivered revision and only environment-dependent behavior in the actual environment. For a skill plugin, check manifest/version alignment, skill discovery and representative tasks in available harnesses. Structural compatibility is not proof of unavailable runtime behavior. Record deployment N/A when there is no deployed service. Confirm PR diffs/review/discussion remain accessible after any source-branch deletion, and link the records rather than deleting PR history.
