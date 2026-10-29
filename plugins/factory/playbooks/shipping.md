# Shipping

Use to integrate and release an already implemented change.

1. Confirm the exact revision's required [Code Review](../skills/code-review/SKILL.md) and [Product Validation](../skills/product-validation/SKILL.md). Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance).
2. Check supported local CI-equivalent results, hosted CI, protection rules, migrations, configuration, dependencies, and release strategy. Return failures to Build.
3. Use [GitHub Workflow](../skills/github-workflow/SKILL.md) to keep target/revision and evidence traceable; merge stacked changes in dependency order under repository policy.
4. Follow [Release](../skills/release/SKILL.md) to verify the intended deployment/environment and live-only risks, with the established recovery path available.
5. Restore and safely synchronize the original checkout; verify the integrated code is present for local use.
6. Clean only safe factory-created merged branches/worktrees after checking dirty work, active use, unmerged commits, and dependent PRs. Preserve the starting/protected branches and PR history.

Proof: accepted revision integrated into the intended target, deployed where applicable, focused environment checks recorded, original checkout restored, and safe cleanup or exact blockers reported. A remote merge alone does not prove local synchronization or deployment.
