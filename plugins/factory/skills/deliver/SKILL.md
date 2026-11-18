---
name: deliver
description: Hand off verified work as a branch, PR, merge, or deployment within the user's requested scope. Use when the accepted change is ready for its authorized destination.
---

# Deliver

Resolve the requested destination from the conversation: local result, branch, PR, merge, or deployment. Preserve that boundary. A branch request is not a merge request. Continue through the authorized work without repeatedly asking for permission already given.

Check that the final content meets the spec, has the applicable verification and review, and has no unresolved material findings. Report missing independent review or runtime evidence rather than inventing acceptance. Use [revision acceptance and safe delivery](../../references/delivery.md) for exact-content receipts, interrupted work, stacked dependencies, synchronization, or cleanup. Its helpers are read-only precondition checks, not authorization.

When creating or updating a PR, inspect the diff and any existing PR first. Lead the description with the problem and resulting behavior, then concise proof and remaining limits. Include actual reviewer outcomes and model/harness attribution when exposed; never guess identities, scores, or usage. Keep prior contributors' credit. A user-requested review branch stays open for their next decision.

For an authorized merge or release, refresh the actual head, target, required checks, review state, and dependency order. Changed content or target invalidates an old receipt. Respect repository protection and unresolved required human review. Use the repository's merge/release path, verify the integrated revision and actual deployment where applicable, and retain the recovery evidence. CI or review failures return to Factory's build/verify loop; a failed premise returns to spec/review.

If asked to monitor a PR, use the harness or repository's existing watcher. Handle real findings and CI failures, verify bot claims, and stop monitoring on handoff. Monitoring does not add merge permission. Publish comments only when authorized.

After authorized integration, safely synchronize the original checkout if possible. Preserve dirty, divergent, active, dependent, or useful work. Delete only Factory-created branches/worktrees whose integration and ownership are proven under the delivery reference. For branch-only work, retain the branch and its evidence for review.

Hand back the result or link, final revision, proof, review status, and any exact unfinished step. A branch can be ready for review while cross-harness adoption or release acceptance is still pending.
