---
name: implementation
description: Deliver focused production changes using maintainable patterns, safe contracts, and local verification. Use for agreed feature and bug-fix code; behavior-preserving structural work belongs to Refactoring.
---

# Implementation

Build the agreed behavior as the smallest complete production change.

## Approach

1. Read the living specification and relevant Codebase Research or Architecture findings.
2. Use existing components, APIs, types, utilities, and conventions before adding new equivalents.
3. Keep changes cohesive, with stable public contracts and responsibilities in the layer that owns them.
4. Implement meaningful success, empty, loading, permission, failure, and transition states when relevant.
5. Follow the shared [code-quality reference](../../references/code-quality.md) and repository/language guidance.
6. Write useful regression checks and run locally reproducible CI checks before pushing.
7. Build in reviewable increments; remove speculative abstractions, temporary scaffolds, and unrelated changes.
8. Return to Requirements/Architecture when implementation reveals a material flaw in the agreed approach.

## Output

Working production code, focused tests, and evidence for independent verification.

## Finish

Requested behavior works, maintainability is preserved, relevant local checks pass. Changes affecting visuals or UI behavior also satisfy the [Factory visual and interface acceptance gate](../factory/SKILL.md#visual-and-interface-acceptance).
