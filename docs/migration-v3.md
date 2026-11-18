# Factory 3 migration

This branch replaces the 2.2.0 capability catalog with six skills. It preserves the original outcome-driven workflow, rendered interface acceptance, project verification tooling, revision-bound delivery checks, and workspace preservation. It makes the return from build/verification to spec/review explicit and bounded.

## Retired entry points

Update personal shortcuts and any project instructions that invoke these names. There are no alias skills: keeping 16 thin forwarding files would preserve the discovery clutter this redesign removes. Git history retains every original skill.

| Previous skill | Current home |
| --- | --- |
| factory | [factory](../plugins/factory/skills/factory/SKILL.md) |
| product-discovery | [spec](../plugins/factory/skills/spec/SKILL.md): problem, evidence, assumptions |
| requirements | spec: outcome, acceptance, revision |
| codebase-research | spec: trace real behavior and constraints |
| architecture | spec: consequential boundaries and alternatives |
| implementation | factory: build loop and project conventions |
| refactoring | factory, with [task-specific proof](../plugins/factory/references/task-proof.md) |
| interface-design | [design](../plugins/factory/skills/design/SKILL.md): experience decisions |
| interface-build | design: translate approved designs and real data |
| prototype | spec/design: disposable experiments only when uncertainty warrants them |
| ui-inspection | design: real rendered states |
| interface-review | design acceptance, coordinated through [review](../plugins/factory/skills/review/SKILL.md) |
| testing | [verify](../plugins/factory/skills/verify/SKILL.md): focused deterministic checks |
| product-validation | verify: original outcome through the real consumer surface |
| code-review | review: evidence, independent judgment, current content |
| github-workflow | [deliver](../plugins/factory/skills/deliver/SKILL.md) and delivery reference |
| release | deliver: authorized integration, release, recovery, synchronization |

The feature, bug-fix, refactor, migration, investigation, and performance playbooks are condensed into task-specific proof. Shipping is part of Deliver. The generic code-quality reference is removed; repository conventions and the few consequential decisions in Factory/Spec/Review cover its useful content. Design references remain because they carry domain judgment.

## What changes operationally

- Spec review and implementation review use the same evidence-based review skill. Reviews remain independent of implementation when the harness permits it.
- Factory defaults to three review passes per cycle and at most two outer returns. The checkpoint carries attempt counts across resumes. A budget ending means unresolved work, not success.
- A defect returns to Build; a failed premise or unprovable approach returns to Spec; an external blocker is reported with its evidence.
- A council is available when requested or warranted. Three same-provider agents are not represented as Theo's three-provider council. Model choices are configurable and availability is disclosed.
- The destination follows the user's request. Preparing a branch or PR does not implicitly authorize merging, deployment, or branch deletion.
- Skill bodies no longer use a universal Approach / Output / Finish template.

## What remains compatible

All three marketplace paths and the `factory-local` / `factory` identity are unchanged. The Python verification and delivery-guard CLI contracts are unchanged, as is `.factory/verification.json`. Design references stay at their existing paths. Historical evaluation requests and receipts stay intact; current skill routing is documented in the evaluation guide rather than rewriting their hashes.

Version 3.0.0 communicates the intentional skill-name break. This branch is a candidate, not a claim of released or installed adoption. Refresh existing plugin caches and confirm discovery in each harness before promoting it. Native Claude Code, Codex, and Cursor runtime acceptance must be recorded separately from portable tests.
