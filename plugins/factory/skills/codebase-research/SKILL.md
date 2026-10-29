---
name: codebase-research
description: Trace real implementation paths, historical rationale, dependencies, and blast radius in an existing repository. Use for system investigation before changing code; rendered interface states belong to UI Inspection.
---

# Codebase Research

Understand how the relevant software works before acting. This investigates the system, not the rendered interface; use [UI Inspection](../ui-inspection/SKILL.md) for actual UI states.

## Approach

1. Read repository instructions, architecture, configuration, and the task.
2. Trace the actual call/data path from entry point to affected behavior.
3. Find existing patterns, contracts, types, tests, consumers, and deployment dependencies.
4. When the reason for a design matters, inspect commits, issues, PRs, and decision records; distinguish evidence from inference.
5. For risky changes, map blast radius beyond direct references and test the critical assumption.
6. For bugs, establish a narrow reproduction and root-cause hypothesis.
7. Stop when the next role has adequate context; avoid indiscriminate repository tours.

## Output

Relevant paths and relationships, important constraints, reusable patterns, root-cause/impact evidence, and unresolved blockers.

## Finish

Material claims are grounded in inspected repository evidence.
