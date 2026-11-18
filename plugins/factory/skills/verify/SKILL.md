---
name: verify
description: Prove a change against the original user outcome through focused checks and the real product surface. Use after implementation and to route failures back to build or spec.
---

# Verify

Read the original request and current spec before evaluating the implementation. Identify the actual revision and dirty/untracked content being tested. An inherited report is context, not proof of the current result.

Run the repository's required checks and the cheapest checks that establish the changed behavior. Prefer an existing test or fixture over a second test framework. For a reproducible bug, observe the failure before the fix when feasible, then repeat the same check. Add regression coverage where it protects meaningful behavior. Avoid tests that repeat types, trivial wiring, or implementation details; a visual adjustment may be best proved by before/after captures.

Exercise the actual consumer surface: UI, API, CLI, generated artifact, or service. Cover the intended task and affected alternate/failure paths. Inspect real integrations where mocks cannot establish the claim. Every visual or UI behavior change also needs [Design's interface acceptance](../design/SKILL.md#interface-acceptance). Keep deterministic checks, implementation review, interface acceptance, and product outcome separate: one cannot stand in for another.

Use [project verification](../../references/verification.md) when launch, health, interaction, evidence, or cleanup instructions are missing or repeated work warrants a reusable contract. Inspect discovered commands before running them. Use isolated fixtures and stop only resources this task started. Unsupported platforms, missing access, or unavailable evidence remain explicit limitations.

Return evidence and PASS / FAIL / INCONCLUSIVE for each applicable acceptance condition and the inspected content. PASS requires observed success; FAIL requires a demonstrated mismatch; INCONCLUSIVE means proof is missing. Overall acceptance requires all applicable conditions to pass. Keep N/A limited to requirements that truly do not apply.

Route findings to [Factory](../factory/SKILL.md): a defect in an otherwise sound approach returns to Build; the wrong outcome, an invalid assumption, or an approach that cannot be proved returns to Spec with the failed observation. A missing credential, unavailable environment, or required human decision is a blocker when no authorized alternative can supply equivalent proof. Do not repeatedly re-spec an access problem, relax the goal, or turn missing evidence into PASS.

After repairs, rerun the affected evidence and relevant integration checks. Reuse unaffected evidence only when its content and assumptions remain valid. An independent validator returns findings to the lead rather than silently repairing the implementation it is assessing.
