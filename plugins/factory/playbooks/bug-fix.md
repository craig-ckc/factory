# Bug fix

Use for an observed failure of intended behavior. Scale proof to the defect; discovery and architecture are optional when evidence reveals a broader problem.

1. Reproduce the symptom in the real affected system. Use [UI Inspection](../skills/ui-inspection/SKILL.md) for rendered UI or the actual API/CLI/service surface otherwise.
2. Trace execution and root cause with [Codebase Research](../skills/codebase-research/SKILL.md); clarify expected behavior with [Requirements](../skills/requirements/SKILL.md) if needed.
3. Preserve failure evidence and a cheap regression check through [Testing](../skills/testing/SKILL.md) when useful.
4. Make the minimal complete fix with [Implementation](../skills/implementation/SKILL.md) or [Interface Build](../skills/interface-build/SKILL.md).
5. Demonstrate passing behavior and relevant nearby boundaries; independently review the actual patch and validate the original affected task. Changes affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../skills/factory/SKILL.md#visual-and-interface-acceptance).
6. Follow [Release](../skills/release/SKILL.md) for integration and delivery.

Proof: failing-before and passing-after for a feasible reproduction, with root-cause evidence and appropriate regression protection. If the failure cannot be reproduced, state the limitation instead of claiming it was fixed by a green build.
