---
name: spec
description: Define or revise a verifiable outcome from a request, repository evidence, or failed verification. Use before substantial implementation or when the current approach cannot meet the goal.
---

# Spec

Start with the user's problem and the evidence already available. Trace the affected behavior, callers, contracts, and existing checks. Look up facts yourself; ask the user only for a consequential decision that the request and evidence cannot settle. A clear task can have a paragraph-sized spec.

Keep one living record in the existing issue, task, or local working note. It needs the intended outcome, scope boundaries, material constraints, and observable acceptance evidence. Separate supplied facts from assumptions. Choose a credible way to prove the outcome before investing in the implementation; green checks for the wrong behavior are not acceptance.

For an architectural decision, compare genuinely different boundaries only where the choice matters. Prefer the smallest coherent model, including removing an existing layer when it obstructs the outcome. Capture the reason a future maintainer could not discover from the code. Use a disposable experiment for a decisive unknown, and record what it proved and what it did not. For experience decisions, use [Design](../design/SKILL.md).

Use [Review](../review/SKILL.md) to challenge the spec: unsupported assumptions, contradictory requirements, missing consumer paths, hidden scope, or an outcome that cannot be verified. Resolve findings and repeat within Factory's loop budget. A reviewer proposing more features is not new authorization. The spec is ready when the outcome and proof are clear and no material finding remains unresolved.

When verification sends work back here, carry the failed observation, current revision, previous attempts, and the assumption that failed. Revise only the affected decisions and proof; retain the original goal and valid evidence. Never weaken an acceptance condition to make the current implementation pass. Re-review the revised spec before building again. A product-intent change requires the user's decision; an implementation change within the agreed outcome normally does not.

Choose [proof appropriate to the change](../verify/SKILL.md#choose-the-proof), including preserved contracts for refactors and recovery constraints for migrations. A request for research or a spec ends at that deliverable unless implementation was also requested.
