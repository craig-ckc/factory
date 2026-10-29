---
name: refactoring
description: Improve software structure while preserving intended externally observable behavior and contracts. Use for transformative maintenance with a concrete structural benefit.
---

# Refactoring

Improve existing code without silently changing what users or callers rely on.

## Approach

1. Identify the specific structural problem and the benefit of changing it.
2. Trace affected consumers, contracts, state, and side effects before editing.
3. Capture baseline behavior through existing tests, examples, or focused characterization checks.
4. Make small transformations that can be evaluated independently.
5. Respect local architecture, naming, and shared [code-quality guidance](../../references/code-quality.md); prefer simplifying over adding abstraction.
6. Verify behavior and interfaces remain equivalent; report intentional semantic changes as separate feature work.
7. Remove dead paths only after dependent usage is checked.

## Output

A smaller or clearer implementation with evidence that its required behavior and contracts were preserved.

## Finish

The structural benefit is concrete, the diff is controlled, and regressions have been ruled out at an appropriate level.
