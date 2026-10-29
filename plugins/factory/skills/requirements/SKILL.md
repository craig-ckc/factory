---
name: requirements
description: Turn the discovered problem or direct request into a focused, reviewable, verifiable specification. Use when defining scope, acceptance conditions, or reviewing material specification gaps.
---

# Requirements

Define the agreed outcome and the behavior necessary to achieve it.

## Approach

1. Start with the original problem and user intent, not an implementation preference.
2. Read relevant product, repository, and discovery evidence before scoping.
3. Define affected actors, behaviors, boundaries, material constraints, and observable acceptance conditions.
4. Identify the cheapest credible verification of the intended result before substantial implementation.
5. Separate required outcomes from optional implementation details; keep the scope proportional.
6. Resolve minor uncertainty from evidence. Escalate only consequential decisions.
7. Ask an independent reviewer to challenge material gaps before Build when delegation is available and permitted. Check ambiguity, missing behavior, contradictions, unsupported assumptions, hidden scope, and unverifiable outcomes. Distinguish independent review from an author self-check.
8. Update the GitHub Issue when evidence changes the solution; preserve the original purpose and rationale. Seek approval for product-intent changes.

## Output

A concise living issue/specification that a builder can implement and an independent validator can assess. Use the established local record when no GitHub workflow exists.

## Finish

Outcome, constraints, and proof are clear; meaningful changes in interpretation are traceable.
