# Performance

Use for a measurable improvement in a user-relevant resource or latency metric. Performance remains a playbook until demonstrated reusable work warrants a standalone skill.

1. Choose a user-relevant metric, representative workload, and success condition.
2. Freeze a repeatable baseline, including environment, data, measurement method, and output correctness.
3. Trace the bottleneck with [Codebase Research](../skills/codebase-research/SKILL.md); test one hypothesis/change at a time through [Prototype](../skills/prototype/SKILL.md) or [Implementation](../skills/implementation/SKILL.md) as appropriate.
4. Compare repeated measurements and correctness with [Testing](../skills/testing/SKILL.md). Account for noise and competing costs.
5. Keep or revert based on evidence; obtain [Code Review](../skills/code-review/SKILL.md) and [Product Validation](../skills/product-validation/SKILL.md) for user-level relevance. Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance).
6. Follow [Release](../skills/release/SKILL.md) only for a demonstrated gain.

Proof: repeatable before/after measurements under comparable conditions, unchanged required behavior, and an improvement relevant to the original task. Report inconclusive results rather than accepting a single noisy run.
