---
name: product-validation
description: Independently verify that a completed change achieves the intended user or business outcome through the real product surface. Use for outcome acceptance, beyond deterministic testing or code review.
---

# Product Validation

Determine whether the completed product solves the accepted problem, not merely whether its code works.

## Approach

1. Start with the original problem, the living specification, and material decisions made since discovery.
2. Define the observable finish condition and use the actual interface, API, CLI, mobile app, generated artifact, or service consumer.
3. Use project-specific verification instructions when available: launch, health check, drive, evidence, cleanup. Discover existing tooling first; establish reusable project-specific instructions when repeated verification justifies them.
4. Exercise the primary task end to end plus meaningful alternate, error, boundary, and permission paths.
5. Confirm external integration and product-level behavior that isolated tests cannot prove. Any change affecting visuals or UI behavior must satisfy the [Factory visual and interface acceptance gate](../factory/SKILL.md#visual-and-interface-acceptance), including an Interface Review PASS for the affected experience.
6. Check whether a technically compliant result still misses user intent. Return consequential mismatch to Requirements; return implementation failures to Build with reproduction evidence rather than repairing code as the independent validator.
7. Report PASS, FAIL, or INCONCLUSIVE for the exact revision with evidence; never equate green CI with user acceptance. Revalidate material changes.

## Output

Outcome-based acceptance verdict, observed behavior, reproduction of failures, and remaining limitations.

## Finish

The result meets the accepted objective, or the gap and its evidence are clear.
