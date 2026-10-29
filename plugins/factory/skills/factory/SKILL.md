---
name: factory
description: Coordinate software changes by selecting relevant skills, requiring interface review for changes affecting visuals or UI behavior, driving evidence-based feedback loops, and preserving the starting workspace.
---

# Software Factory

Use the skills needed to turn a problem into verified, maintainable software. Roles are responsibilities, not fixed agents or providers. Repository instructions and established conventions provide the project-specific context.

## Defaults

- Prefer small, complete changes, clear contracts, and existing conventions.
- Preserve the user's actual problem; revise the proposed solution when new evidence warrants it.
- Verify observable behavior, not just that code builds.
- Keep deterministic verification local where practical; use live environments for what only they can prove.
- Add complexity, parallel agents, and artifacts only when they solve a real problem and delegation is permitted.

## Flow

Input → Define (spec ⇄ independent review) → Build (code ⇄ verify) → Deliver (validate → ship).
Loop backward when evidence changes the scope. For small work, skip unnecessary ceremony.

Scope establishes the outcome; Review challenges it; Code builds; Verify checks; Test exercises the real result; Ship integrates and releases. Compose capabilities as needed, rather than assigning an agent to each skill.

## Visual and interface acceptance

Any change that affects visuals or the behavior of a user interface requires [Interface Review](../interface-review/SKILL.md) before completion. Select capabilities from the full effect of the change, not just its task label or playbook. This gate applies to every playbook, including migrations and refactors, and to changes made without editing code. Small changes and reuse of existing components are not exemptions. An image replacement or an animation adjustment still needs review; these examples do not limit the scope of the rule.

Establish the intended experience and affected surfaces before implementation. Use [Interface Design](../interface-design/SKILL.md) when experience decisions are unresolved, and [UI Inspection](../ui-inspection/SKILL.md) to exercise the actual result. Scale review effort to the change without skipping it.

Require both visual acceptance and functional verification for the changed result. Inspect the rendered interface in the relevant supported contexts, including behavior over time where affected. Verify that changed assets and dependencies actually work in those contexts; checking a URL or a source diff alone is not enough. Use [Testing](../testing/SKILL.md) for deterministic checks that complement the rendered review.

Have a reviewer other than the implementer perform Interface Review when delegation is available and authorized. Otherwise perform a separate review pass and disclose that independent review was unavailable. Record the inspected revision, scope, evidence, and PASS/FAIL/INCONCLUSIVE verdict. Resolve introduced defects, including visual defects, and review the affected result again before marking the work complete. Missing evidence is INCONCLUSIVE, not PASS; a successful build or code review does not satisfy this gate.

## Capability routing

Read the relevant skill on demand; do not load the whole inventory.

| Domain | Capabilities |
| --- | --- |
| Understand | [Product Discovery](../product-discovery/SKILL.md) for unclear problems; [Requirements](../requirements/SKILL.md) for agreed outcomes; [Codebase Research](../codebase-research/SKILL.md) for implementation paths; [Architecture](../architecture/SKILL.md) for consequential structure |
| Engineer | [Implementation](../implementation/SKILL.md) for production changes; [Refactoring](../refactoring/SKILL.md) for behavior-preserving structural improvements |
| Design | [Interface Design](../interface-design/SKILL.md) for experience decisions; [Interface Build](../interface-build/SKILL.md) for production translation; [Prototype](../prototype/SKILL.md) for disposable experiments; [UI Inspection](../ui-inspection/SKILL.md) for running states; [Interface Review](../interface-review/SKILL.md) for independent quality assessment |
| Verify | [Testing](../testing/SKILL.md) for deterministic checks; [Product Validation](../product-validation/SKILL.md) for actual outcomes; [Code Review](../code-review/SKILL.md) for implementation risks |
| Deliver | [GitHub Workflow](../github-workflow/SKILL.md) for repository evidence and history; [Release](../release/SKILL.md) for merge, deployment, recovery, and restoration |

Design and Engineering may iterate together. Discovery, Architecture, Prototype, and Refactoring are conditional capabilities, not mandatory stages. Performance remains a playbook.

Choose one task playbook when useful: [Feature](../../playbooks/feature.md), [Bug Fix](../../playbooks/bug-fix.md), [Refactor](../../playbooks/refactor.md), [Migration](../../playbooks/migration.md), [Investigation](../../playbooks/investigation.md), [Performance](../../playbooks/performance.md), or [Shipping](../../playbooks/shipping.md). Adapt its sequence and proof to the task.

## Records

- GitHub Issue = living problem, intended outcome, accepted specification, and substantive decisions.
- PR = exact implementation, tests, independent review, and supporting evidence.
- Record when discovery materially changes the solution; obtain approval if it changes the intended product outcome.
- Use existing local records when there is no GitHub workflow; do not introduce remote artifacts merely for ceremony.

## Workspace integration

Record the starting branch, upstream, and uncommitted work; never assume `main`. Isolate work where useful and preserve pre-existing changes. Run relevant local CI-equivalent checks and obtain patch-specific independent acceptance where required. Respect approvals and protected branches; integrate to the intended target, synchronize and verify the original checkout, and clean only safe factory-created merged branches/worktrees. On blockers, preserve work and report the exact unfinished step. Detailed repository mechanics belong to GitHub Workflow and Release.

## Continuity

For long runs, keep a small resumable checkpoint: goal, branch/worktree, completed evidence, open PRs, and next step. Prefer enforceable tests, lint, types, or architectural boundaries over ever-growing instruction files.

Use [Learning and regression evaluation](../../references/learning.md) when observed failures justify a reusable improvement or before promoting material Factory revisions. Distinguish recurring history from seeded cases; compare representative baseline/candidate tasks and preserve successful behavior. Detailed checkpoint and exact-revision delivery mechanics belong to [GitHub Workflow](../github-workflow/SKILL.md) and [Release](../release/SKILL.md).
