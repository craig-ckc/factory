---
name: interface-build
description: Translate approved Figma frames, screenshots, or interface specifications into production UI and prove visual fidelity. Use for design-to-code work within the existing product.
---

# Interface Build

Implement the intended design within the real product.

## Approach

1. Read the approved design and original source (Figma, images, specs), alongside the existing component library and tokens. For Figma work, follow the available Figma integration skills and tools; if access is unavailable, identify the missing source rather than inventing values.
2. Treat source design values as exact when available; label screenshot-derived dimensions as estimates.
3. Reuse matching components and tokens. Propose a new token/variant when justified; never silently distort a visible design.
4. Implement only the requested surfaces and realistic responsive/interaction states; don't redesign adjacent screens.
5. Wire actual data paths where available; explicitly identify mocked or unwired behavior.
6. Run the UI at relevant widths and compare against reference images side by side; inspect missing, error, and keyboard states where meaningful. When exact visual parity is required, keep an immutable reference and use rendered image differences; ordinary design work does not require zero pixel difference.
7. Escalate conflicts between approved visuals and accessibility/technical constraints rather than hiding deviations.

Read the relevant shared [layout](../../references/design/layout.md), [typography](../../references/design/typography.md), [color](../../references/design/color.md), [accessibility](../../references/design/accessibility.md), [interface-writing](../../references/design/interface-writing.md), and [motion](../../references/design/motion.md) guidance only as needed.

## Output

Production UI, visual comparison evidence, and a concise list of deviations or unresolved design decisions.

## Finish

The interface matches the intended design, fits the existing product, and satisfies the [Factory visual and interface acceptance gate](../factory/SKILL.md#visual-and-interface-acceptance) for the affected experience.
