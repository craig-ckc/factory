# Migration

Use when replacing an implementation, dependency, interface, or data representation with compatibility and rollout constraints.

1. Inventory producers, consumers, versions, data, deployment dependencies, and rollback/recovery constraints with [Codebase Research](../skills/codebase-research/SKILL.md).
2. Define target behavior and compatibility in [Requirements](../skills/requirements/SKILL.md); use [Architecture](../skills/architecture/SKILL.md) to choose a safe sequence when boundaries change.
3. Establish a baseline and executable contract checks before changing data or callers.
4. Migrate in independently verifiable increments through [Implementation](../skills/implementation/SKILL.md). Preserve a recovery path appropriate to the actual migration.
5. Verify integration, data behavior, and consumer outcomes with [Testing](../skills/testing/SKILL.md), [Code Review](../skills/code-review/SKILL.md), and [Product Validation](../skills/product-validation/SKILL.md). Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance).
6. Remove legacy paths only when dependent usage is resolved; follow [Release](../skills/release/SKILL.md) for ordered rollout and focused live verification.

Proof: target producers and consumers work together, data/contracts remain valid, and recovery constraints are understood. Do not infer data safety solely from successful compilation.
