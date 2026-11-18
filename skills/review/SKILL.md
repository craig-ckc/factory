---
name: review
description: Challenge a spec or implementation with evidence and bounded independent review. Use for acceptance, consequential design decisions, or a requested review council.
---

# Review

Fix known defects and run relevant checks before requesting review. Identify the goal, excluded scope, spec version or diff base and current content, and available proof. Include untracked files that belong to the change. Reviewers inspect that snapshot read-only; they do not edit, publish, or recruit more reviewers. Hold the reviewed files stable until the pass finishes, or give reviewers isolated snapshots.

Use one independent reviewer by default when available and permitted. For consequential or disputed decisions, a council can supply independent perspectives. Respect explicitly requested members and model/provider settings in the user's instructions or project configuration. Discover actual capabilities instead of hardcoding model IDs. Theo's council uses three providers: if that is requested and unavailable, report the gap; several instances of one model are not a multi-provider council. An ordinary same-provider review remains useful if its limits are disclosed. Without delegation, perform a separate self-review and identify it honestly; a self-review cannot satisfy a required independent gate.

Give each reviewer the same question and enough source context to check it independently. For a spec, challenge whether the intended outcome and proof are sound. For implementation, trace relevant callers and failure paths, check the original intent, and inspect unnecessary complexity as well as bugs. For interfaces, apply [Design's acceptance requirements](../design/SKILL.md#interface-acceptance). Skip speculative improvements outside the task.

Ask for concrete findings: stable ID, location, consequence, evidence, severity, and smallest useful correction. A blocker prevents the intended outcome; a material finding is a real defect within scope; a nit is an optional preference or follow-up. Do not use a numeric score or majority vote to erase a demonstrated defect.

The lead checks every finding against source or observed behavior. Fix agreed defects, reject false positives with evidence, and keep unrelated improvements as follow-ups. Record the disposition in the existing working record. Preserve useful disagreement rather than changing code just to please a reviewer. Synthesize council findings and overlapping issues before editing.

Follow [Factory's loop budget](../factory/SKILL.md#progress-and-stopping). The first pass covers the scope; later passes cover changed behavior and unresolved findings. Re-review material fixes on the current content. Declined nits or purely editorial fixes need no new full review, though any exact-revision delivery receipt must be refreshed. Report APPROVE, CHANGES, or INCONCLUSIVE with the reviewed content and coverage. A timeout, unavailable reviewer, unresolved material disagreement, or exhausted budget is never approval.
