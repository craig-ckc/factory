---
name: factory
description: Take a software task through spec/review and build/verify loops, returning failed assumptions to the spec before delivering the requested result.
---

# Factory

Own the user's outcome from input to the requested handoff. Use the existing repository, tools, conventions, and task record. Keep the process proportional: a clear fix needs a short spec and focused proof, not a planning ceremony.

Read the relevant skill at the point it is needed. Factory owns sequencing and implementation; capabilities are responsibilities, not a roster of agents.

## Input

Establish the goal, available context, constraints, and delivery destination. Inspect the current work and starting branch/upstream; preserve pre-existing changes. Resume from current evidence rather than replaying a stale plan. Use an isolated branch or worktree where useful.

## Spec ↔ review

Use [Spec](../spec/SKILL.md) to define the smallest complete outcome and how to prove it. Resolve meaningful design uncertainty with [Design](../design/SKILL.md). Use [Review](../review/SKILL.md) to challenge the spec, then revise it until the outcome, constraints, and evidence are credible and no material finding remains open. Use independent review when available and permitted; disclose self-review.

A revised implementation approach within the authorized outcome does not need a new permission round. A consequential change to the user's intended product outcome does. Research-only or spec-only work stops at the requested deliverable.

## Build ↔ verify

Implement a complete, reviewable slice of the accepted spec. Prefer deleting or narrowing code to adding speculative layers. Preserve required contracts and migrate callers before removing old paths. The agent already knows how to code; use project instructions for implementation details and [task-specific proof](../../references/task-proof.md) for special constraints.

Use [Verify](../verify/SKILL.md) against the original goal and current spec, and [Review](../review/SKILL.md) on the actual implementation. Changes to visuals or UI behavior must satisfy [Design's interface acceptance](../design/SKILL.md#interface-acceptance). Fix demonstrated defects and repeat the affected checks/review on the new content.

## The outer loop

| Evidence | Next action |
| --- | --- |
| Implementation fails a sound acceptance condition | Return to Build with the reproduction; verify the repair. |
| Intended behavior is wrong, an assumption fails, or the chosen approach cannot be verified | Return to Spec with the evidence; revise and review before building again. |
| Required proof is blocked by access, environment, or a human decision and no authorized equivalent is available | Preserve the checkpoint and report the exact blocker. |
| Verification passes and review has no unresolved material finding on current content | Deliver to the requested destination. |

A return to Spec carries the original goal, failed observation, attempts, affected decisions, and still-valid evidence. Keep the same task; do not launch another Factory agent or recursively restart the workflow. The loops are feedback, not nested agent spawning.

## Progress and stopping

Keep a compact checkpoint for work that spans rounds or sessions: goal/spec revision, branch and inspected content, current loop, findings and dispositions, evidence, attempts, and next action. Reuse the existing issue/task or local note; no prescribed document template or new tracking system is needed.

Default to three review passes per spec or implementation cycle, reviewing changed behavior and open findings after the first. Allow at most two returns from Build/Verify to Spec in one run. These limits are Factory defaults, not a claim about Theo's council. Count returns across revisions and resumes; changing the spec or reviewer does not reset the outer budget. Stop earlier when the same material finding survives two repair attempts without new evidence. The user can extend the budget. Nits alone do not justify another round. Budget exhaustion or disagreement leaves the work blocked or inconclusive, never approved.

Continue independent useful work while a genuine blocker is pending. If no authorized work remains, hand back the evidence and the smallest decision or capability needed to resume. Never weaken acceptance to get out of a loop.

## Deliver and learn

Use [Deliver](../deliver/SKILL.md) for the authorized handoff. Merge, deployment, and cleanup are separate destinations and conditions, not automatic consequences of running Factory.

Use [learning and regression evaluation](../../references/learning.md) when an observed failure warrants a reusable improvement or when changing Factory itself. Prefer a test, type, boundary, or tool to an ever-growing instruction file. Preserve effective behavior while removing unnecessary process.
