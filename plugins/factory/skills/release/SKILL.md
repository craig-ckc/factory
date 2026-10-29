---
name: release
description: Supervise accepted changes through merge, deployment, recovery, workspace restoration, and focused live verification. Use after implementation acceptance when shipping a revision.
---

# Release

Ship an independently accepted revision through the repository's actual delivery path.

## Approach

1. Confirm independent Code Review and Product Validation for the exact revision where required. Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../factory/SKILL.md#visual-and-interface-acceptance), including an Interface Review PASS. Re-check acceptance after changes to the reviewed result.
2. Inspect CI, protection rules, migrations, config, dependencies, and release/deployment strategy.
3. Resolve failures in Build; do not merge on incomplete or outdated verification.
4. Merge stacked changes in safe dependency order under repository policy, using the established merge strategy once required gates pass. Honor existing authorization and explicit human approval gates.
5. Observe release/deployment through completion and verify the intended revision reached the intended environment; check only live-dependent behavior in production.
6. Capture delivery failures and use the established recovery/rollback path.
7. Return the original checkout to its recorded starting branch; synchronize safely and verify integrated code is locally present. Follow [GitHub Workflow](../github-workflow/SKILL.md) for local/remote integration and safe branch hygiene.
8. Remove only safely integrated factory-created worktrees/merged topic branches, never dirty or dependent work.
9. Record release evidence and meaningful operational follow-up in the PR or issue. Feed live findings into subsequent work when relevant without requiring permanent operations ceremony.

## Output

Use [Revision acceptance and safe delivery](../../references/delivery.md) for checkpoint fields, changed-head/target invalidation, dependency ordering, local synchronization, squash/rebase constraints and post-release adoption evidence. Refresh actual state on resume and immediately before any cleanup; a prior guard result is not lasting deletion authority.

Merge/deployment outcome, tested revision and environment, local workspace state, and precise unresolved blockers.

## Finish

Change is safely integrated and observable; otherwise the system and evidence are preserved for recovery.
