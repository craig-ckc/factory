---
name: code-review
description: Independently inspect an implementation diff for correctness, security, contracts, regression risk, and maintainability. Use for patch review; specification review belongs to Requirements and interface quality to Interface Review.
---

# Code Review

Challenge the implementation that is actually proposed for integration.

## Approach

1. Review the agreed outcome, changed patch, relevant contracts, tests, and runtime context.
2. Trace important changed paths instead of judging only the local diff.
3. Look for incorrect behavior, security/data risks, missed requirements, regressions, breaking changes, unnecessary complexity, and weak verification.
4. Use Architecture and shared [code-quality guidance](../../references/code-quality.md) for maintainability; distinguish consequential defects from style preferences.
5. Validate critical claims using code, tests, repros, or logs, and prioritize findings by real impact.
6. Remain independent of the author when the workflow permits. Do not rewrite implementation while acting as independent reviewer; disclose when only a self-check is available.
7. Attach approval to the actual patch/revision; revisit materially changed code after fixes.
8. Give concrete location, consequence, and reproduction or evidence for each finding.

For high-risk or contested work, seek independent alternative analysis when permitted and test decisive blast-radius assumptions rather than producing speculative risk lists.

## Output

Approval or a concise, prioritized list of actionable findings, with reviewed revision and coverage.

## Finish

No known material defect blocks the reviewed revision; uninspected scope is not silently approved.
