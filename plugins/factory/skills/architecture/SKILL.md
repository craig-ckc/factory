---
name: architecture
description: Decide software boundaries, responsibilities, interfaces, and dependency direction for consequential changes. Use when a structural decision has lasting consequences.
---

# Architecture

Choose structure that fits the existing system and the problem.

## Approach

1. Inspect the current architecture and affected runtime boundaries first.
2. Define ownership, module boundaries, data flow, contracts, error handling, and dependency direction.
3. Prefer one coherent established pattern over introducing a parallel system.
4. Compare two structurally different approaches only when the decision has lasting consequences.
5. Validate a decisive assumption with a small experiment or contract check if cheaper than speculation.
6. Add abstractions when they stabilize a boundary or remove real duplication, not merely for neatness.
7. Preserve rationale only for architectural decisions future maintainers must understand.

## Output

A focused design decision: placement, ownership, interfaces, tradeoffs, and any lasting constraints.

## Finish

Contracts and dependencies are clear; complexity is proportional and implementation can proceed.
