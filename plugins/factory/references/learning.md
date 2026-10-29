# Learning and regression evaluation

Use when a review, test failure, revert, or repeated task exposes a reusable failure class, or before promoting a material Factory skill revision. Do not turn every incident into a permanent instruction.

Inspect linked review/revert/test history. Group failures by underlying mechanism, retain concrete evidence, and distinguish a demonstrated recurrence from a single incident or seeded evaluation. Record: failure class → observed examples → cause → proposed intervention → executable evidence → decision. With no meaningful history, state that limitation and use clearly labeled representative cases.

Prefer a stable architecture boundary, type contract, lint rule, or behavior test over more prose. Add a skill rule only when a decision genuinely needs contextual judgment. Reject interventions that fix one example while expanding unrelated scope or approval requirements.

Before promoting a substantial skill change:

1. Freeze baseline/candidate source identities and the same small outcome-oriented request set, fixtures, tools, and permitted side effects.
2. Have task-performing agents use the applicable skills on realistic requests. Keep the rubric and intended answers with a separate evaluator. When delegation is unavailable, disclose that the evaluation is a self-check.
3. Retain prompts, actual outputs/tool evidence, rubric, inspected revision or content digest, and independent PASS/FAIL/INCONCLUSIVE decisions. Evaluate important failures and original intent, not whether the response repeats new headings or invokes a candidate-only helper.
4. Compare cases fairly. Preserve baseline successes, explain gains/regressions and unresolved uncertainty, and rerun affected cases after material fixes. A small task set supports only its covered behaviors.
5. Promote only after relevant deterministic checks, independent review, and representative behavioral acceptance. Preserve evidence when blocked or inconclusive; do not claim an unavailable provider passed.

This repository's maintained cases and comparison procedure live in [evaluations](../../../evaluations/README.md). The packaging check prevents inconsistent cross-agent versions and broken skill references; helper tests exercise stale acceptance and unsafe cleanup. These are seeded executable regressions, not fabricated historical incidents. Keep learning records with the existing issue/PR rather than growing a second issue system.
