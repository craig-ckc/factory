# Refactor

Use for a concrete structural improvement while preserving externally observable behavior. [Refactoring](../skills/refactoring/SKILL.md) is also a capability usable inside another task when warranted.

1. Name the structural defect, expected benefit, and preserved behavior/contracts.
2. Map consumers, side effects, and blast radius with [Codebase Research](../skills/codebase-research/SKILL.md); use [Architecture](../skills/architecture/SKILL.md) for lasting boundary decisions.
3. Capture a baseline through existing tests, examples, or targeted characterization checks.
4. Refactor in small independently checkable transformations, using shared [code-quality guidance](../references/code-quality.md).
5. Compare behavior/contracts against the baseline; verify integration and meaningful user-visible paths where affected. Remove dead paths only after checking consumers.
6. Obtain [Code Review](../skills/code-review/SKILL.md), satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance) for changes affecting visuals or UI behavior, and follow [Release](../skills/release/SKILL.md).

Proof: a controlled structural benefit with equivalent required behavior and contracts. Treat intentional semantic changes as separate feature scope.
