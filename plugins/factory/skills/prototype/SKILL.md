---
name: prototype
description: Resolve design or technical uncertainty through focused, disposable, testable experiments and alternatives. Use when a specific unresolved question warrants a prototype or feasibility spike.
---

# Prototype

Build just enough to learn; never confuse a prototype with production code.

## Approach

1. State the question and decision the experiment must answer.
2. Reuse existing previews, mocks, design tools, or Storybook before creating new app routes.
3. For competing interface variants, vary a meaningful primary axis (structure, density, emphasis, or interaction) rather than superficial styling.
4. Keep prototypes realistic enough to expose tradeoffs, with plausible data and correct surrounding context.
5. When necessary, include technical spikes to test feasibility, data behavior, or performance assumptions.
6. Present alternatives with evidence, limitations, and costs; leave product-direction decisions to the user when consequential.
7. Promote the chosen solution through [Interface Build](../interface-build/SKILL.md)/[Implementation](../implementation/SKILL.md). Remove throwaway code only after it is no longer needed and no useful work is lost.

For interface experiments, load only relevant shared guidance from [Interface Design](../interface-design/SKILL.md).

## Output

A testable experiment, what was learned, the decision still required, and a cleanup path.

## Finish

The original uncertainty is reduced without leaving permanent speculative infrastructure.
