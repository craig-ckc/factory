---
name: github-workflow
description: Coordinate Git issues, branches, commits, PRs, review evidence, and safe repository history. Use for repository workflow, distinct from deployment and Release.
---

# GitHub Workflow

Use Git/GitHub as the durable record of scope, implementation, reviews, and evidence.

## Approach

1. Keep the Issue as the living specification; preserve original intent and significant scope decisions. Use established local records when no remote workflow exists.
2. Record the repository, starting branch/upstream, and pre-existing uncommitted work.
3. Use focused commits and isolated topic branches/worktrees when useful. Keep unrelated work outside the change.
4. Link issue, PR, test runs, review verdict, exact patch, and delivery evidence rather than duplicating reports.
5. Run supported local CI-equivalent checks before pushing; investigate real failures, don't hide them. Use existing CI runs and logs to return failures to Build.
6. Respect branch protection, required checks, approvals, and dependent PRs. Resolve review findings and re-review material fixes.
7. Preserve useful history; never force-delete useful work or assume `main` is the user's original integration target.

## Integration and branch hygiene

For local-only work, integrate completed changes into the recorded starting branch. For remote work, use a PR targeting the intended branch, then synchronize the original checkout with the remote result; a remote merge does not update it automatically. Prefer fast-forward synchronization. Resolve divergence/conflicts deliberately and preserve the user's pre-existing changes; report a blocked step rather than discarding work.

Delete only safely merged factory-created topic branches/worktrees. Check dirty work, unmerged commits, active use, and dependent PRs first. Preserve the starting branch and default/protected branches. Use the app's managed-worktree lifecycle tools when they own the checkout. Merged GitHub PR discussion, reviews, and diffs remain after deleting its merged source branch; retain the PR and linked evidence.

## Output

A traceable issue/PR history and safe branch/worktree state.

## Finish

The target and revision are unambiguous, evidence is linked, and no unrelated work was discarded.
