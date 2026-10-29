# Feature

Use for a new or changed product behavior. Select capabilities to fit the uncertainty and risk; this sequence is a guide, not a mandatory skill chain.

1. Confirm the intended outcome and affected users. Use [Product Discovery](../skills/product-discovery/SKILL.md) only when the problem or solution is materially uncertain.
2. Trace current behavior with [Codebase Research](../skills/codebase-research/SKILL.md), then scope and independently review the living issue with [Requirements](../skills/requirements/SKILL.md).
3. Select [Interface Design](../skills/interface-design/SKILL.md), [Architecture](../skills/architecture/SKILL.md), or [Prototype](../skills/prototype/SKILL.md) only where needed. Design and Engineering may iterate together.
4. Implement a complete slice through [Implementation](../skills/implementation/SKILL.md) and [Interface Build](../skills/interface-build/SKILL.md) as relevant.
5. Run focused [Testing](../skills/testing/SKILL.md), [Code Review](../skills/code-review/SKILL.md), and independent [Product Validation](../skills/product-validation/SKILL.md). Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance).
6. Use [Release](../skills/release/SKILL.md) once the required acceptance and checks apply to the actual patch.

Proof: the affected user can complete the agreed task through the real product surface, with relevant alternate/failure behavior established. Preserve the original problem when refining the proposed solution.
