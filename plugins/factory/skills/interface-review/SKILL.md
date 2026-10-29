---
name: interface-review
description: Review every change affecting visuals or UI behavior, including asset-only and motion-only changes. Independently assess the actual experience, accessibility, visual quality, and regressions, distinct from implementation Code Review.
---

# Interface Review

Evaluate the actual product interface, not personal stylistic preferences.

Apply the [Factory visual and interface acceptance gate](../factory/SKILL.md#visual-and-interface-acceptance) regardless of the selected playbook or apparent simplicity of the change. Review the full affected experience, not a closed checklist of UI properties. Asset replacements and changes over time are included even when structure and styling are unchanged.

## Approach

1. Scope the affected screens or PR diff; trace changed components to user-visible surfaces.
2. Inspect design-system context and the user problem before passing judgment.
3. Review what users see and how the interface behaves, including changes over time, in the relevant supported contexts. Use relevant shared references: [layout](../../references/design/layout.md), [typography](../../references/design/typography.md), [color](../../references/design/color.md), [accessibility](../../references/design/accessibility.md), [interface writing](../../references/design/interface-writing.md), [motion](../../references/design/motion.md). These references guide judgment; they do not define the limits of review.
4. Classify each issue as introduced, regression, or pre-existing; avoid blocking a change on unrelated existing defects.
5. Verify the changed result with rendered evidence and appropriate functional checks. Confirm that assets load and behave correctly through the product in the relevant supported environments; a reachable URL alone does not prove that. Use interaction or time-based evidence when a still image cannot establish the result. Record reproducible findings, source paths, and actual content.
6. Prioritize issues by user impact, but resolve introduced visual and functional defects before a PASS. Lower severity determines repair order, not whether a visible defect may be dismissed as polish. Route repairs back to the implementer and review the affected result again.
7. Return actionable findings to Design/Interface Build without rewriting implementation while acting as independent reviewer.

## Output

Scope and coverage, prioritized findings with reproduction/evidence, and PASS/FAIL/INCONCLUSIVE verdict for the inspected revision and requested change.

## Finish

The approval applies only to the revision, interfaces, states, and supported contexts actually inspected. Missing evidence requires INCONCLUSIVE. Completion requires a PASS for the affected experience; re-review the affected result after fixes.
