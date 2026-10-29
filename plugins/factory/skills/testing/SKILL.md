---
name: testing
description: Select and run deterministic automated checks that establish changed behavior and prevent reproducible regressions. Use for test selection, failure reproduction, or regression protection; product acceptance belongs to Product Validation.
---

# Testing

Reduce reproducible uncertainty at the cheapest reliable level.

## Approach

1. Derive checks from behavior, acceptance criteria, contracts, edge cases, and risk.
2. Prefer existing static/type, unit, integration, contract, end-to-end, or platform test infrastructure.
3. For bugs, reproduce failure before the fix when feasible; add regression protection where it pays off.
4. Use behavior-oriented assertions and cover meaningful failures and state transitions.
5. Control flaky network, timing, and mutable data unless those are the thing being tested.
6. Run locally reproducible checks early, preferably using the same commands as CI. Leave unsupported platform or hosted-only checks to the appropriate runner and report the limitation.
7. Don't duplicate expensive tests for vanity coverage or weaken assertions to make them pass.
8. Report exactly what ran, passed, failed, or could not run.

For performance claims, follow the [Performance playbook](../../playbooks/performance.md) to establish a representative workload, repeatability, and correct output.

## Output

Focused durable tests and reproducible results, with remaining uncertainty explicit.

## Finish

Relevant deterministic behavior has been established without claiming broader acceptance than tests prove.
