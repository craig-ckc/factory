---
name: design
description: Shape, build, and inspect interfaces, including approved-design translation, asset changes, and motion. Use whenever work affects visuals or UI behavior.
---

# Design

Ground the experience in the user's task, existing product, real content, and supplied design. Reuse the design system. Resolve the interaction model, hierarchy, affected surfaces, and meaningful states before committing to a visual direction. Prototype competing directions only when an unresolved decision warrants it; keep experiments disposable.

When translating an approved design, preserve its intent and inspect the actual source frames, assets, and dimensions. Map them to existing components and tokens. Surface a material conflict with accessibility or technical constraints rather than quietly redesigning it. Wire the real data path where available and identify any remaining mocks.

Load only the guidance needed for the change: [layout](../../references/design/layout.md), [typography](../../references/design/typography.md), [color](../../references/design/color.md), [accessibility](../../references/design/accessibility.md), [interface writing](../../references/design/interface-writing.md), or [motion](../../references/design/motion.md).

## Interface acceptance

Every change affecting visuals or UI behavior needs rendered inspection, including asset-only changes, animation, migrations, refactors, and edits made without code. Scale the inspection to the effect of the change. Small size or reuse of a component is not an exemption.

Exercise the real interface in relevant supported contexts. Check the affected entry points, responsive layout, content, keyboard/focus, and loading, empty, error, permission, or transition states where they matter. A temporary workbench should use the actual component, not a lookalike. Verify that assets load and behave through the product; a reachable URL or source diff is insufficient. Use time-based evidence when a screenshot cannot establish motion or interaction. For exact design parity, retain the reference and compare rendered images; ordinary design work does not require zero pixel difference.

Have an independent reviewer inspect the result when available and permitted; otherwise make a separate pass and disclose the lack of independence. Use [Review](../review/SKILL.md) for findings and [Verify](../verify/SKILL.md) for functional evidence. Distinguish introduced defects, regressions, and unrelated pre-existing problems. Resolve introduced visual and functional defects, then inspect the affected result again. Preference alone is not a defect, and calling an observed defect “polish” does not waive it.

Record the inspected revision, surfaces and states, evidence, and PASS / FAIL / INCONCLUSIVE. Missing rendered evidence is INCONCLUSIVE. A successful build, test suite, or code review cannot supply an interface PASS.
