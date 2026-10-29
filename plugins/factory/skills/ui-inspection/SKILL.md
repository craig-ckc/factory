---
name: ui-inspection
description: Exercise existing interface components and user journeys to expose reachable states, responsive issues, and failure conditions. Use for real rendered behavior rather than architecture research or building alternatives.
---

# UI Inspection

Observe how the actual interface behaves; this is distinct from tracing backend code.

## Approach

1. Identify the real screen/component, its inputs, and its reachable states.
2. Reuse the running app, Storybook, existing fixtures, browser tests, or preview routes.
3. Exercise loading, empty, error, permissions, long content, narrow viewports, keyboard/focus, and meaningful transitions as applicable.
4. If existing tools cannot expose states, make a temporary workbench using the real component with data supplied at its boundary; do not rebuild a lookalike.
5. Record actual rendered behavior and reproduction steps, not assumptions based only on JSX/CSS.
6. Avoid an exhaustive cross-product of artificial states; target plausible and high-risk conditions.
7. Keep temporary harnesses isolated, remove them when no longer needed, and preserve useful evidence.

Use shared [layout](../../references/design/layout.md) and [accessibility](../../references/design/accessibility.md) checks when relevant. An observation is not an independent [Interface Review](../interface-review/SKILL.md) verdict or [Product Validation](../product-validation/SKILL.md) acceptance.

## Output

Observed states, defects or constraints, reproducible steps, and screenshots/logs where relevant.

## Finish

Important interface states have been exercised through real rendering or explicitly marked unverified.
