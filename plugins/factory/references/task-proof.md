# Task-specific proof

Read the applicable case while defining acceptance; these are variations within Factory's loops, not separate workflows.

| Task | Evidence that changes the decision |
| --- | --- |
| Feature | The affected user completes the intended task through the real product, including relevant alternate and failure paths. Preserve the problem when revising the proposed solution. |
| Bug fix | The original failure reproduces where feasible, its cause is established, and the same reproduction passes after the fix. A green build alone cannot prove a fix. |
| Refactor | A concrete structural benefit with preserved required behavior and consumer contracts. Compare against the baseline and check callers before deleting old paths. Name intentional semantic changes explicitly. |
| Migration | Producers, consumers, data, and supported versions work through the transition. Establish compatibility, order, and a recovery path before changes; retire legacy paths only after dependent usage is resolved. |
| Performance | Repeated before/after measurements on a representative workload with comparable environment and correct output. Account for noise and competing costs; one faster sample is inconclusive. |
| Investigation | Inspected paths, observed behavior, and an experiment that settles the question where feasible. Separate facts from inference. Stop at findings when implementation is outside the request. |

All interface changes still require [rendered acceptance](../skills/design/SKILL.md#interface-acceptance). Delivery uses [Deliver](../skills/deliver/SKILL.md) after the applicable proof is established.
