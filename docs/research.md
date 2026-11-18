# Research behind Factory 3

Research date: 2026-11-18. This is a comparison of published instructions and repository design, not a claim to reproduce anyone's complete personal philosophy. Theo receives the most weight. The implementation is an original synthesis; it does not vendor their skills or inherit their permissions.

## Sources and identity

“Grilly” is treated as Matt Pocock's **grill-me**, whose current implementation delegates to **grilling**. “Potato” is treated as **poteto**, the author of Brainmaxxing and the verification-skill example. Employment and acquisition claims were not needed for this design and were not independently verified.

Theo's agent skill repository is **t3dotgg/tstack**. This is distinct from the T3 Stack application starter and from **pingdotgg/t3code**, the coding-agent application. Council is a tstack skill. T3 Code's repository instructions add useful implementation evidence, but they are team/project guidance unless explicitly marked as Theo's own note.

Pinned source snapshots:

| Source | Revision | What was inspected |
| --- | --- | --- |
| [Theo: tstack](https://github.com/t3dotgg/tstack/tree/11e37a74d0a6868c121cd0910ab2b3bd9873b92a) | `11e37a74` | README and all nine SKILL.md files |
| [T3 Code](https://github.com/pingdotgg/t3code/blob/316c3256a3a09cef7ed68914ebe74c7183ac08e1/AGENTS.md) | `316c3256` | Theo's note, testing, documentation, workflow, safety and architecture guidance |
| [Matt: skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | `5863806d` | README, grill-me, grilling, writing-for-agents, repository layout |
| [Poteto: Brainmaxxing](https://github.com/poteto/brainmaxxing/tree/ec4d8e43dee639d6f5d94aed3ca16af7b298ecfc) | `ec4d8e43` | README, plan, review, encode-lessons-in-structure, subtract-before-you-add |
| [Poteto: verification example](https://github.com/poteto/verification-skill-example/blob/d5abe70d0d8c671672b6cef4069363f26c488feb/README.md) | `d5abe70d` | Scoped verification and behavior-level feature-map rationale |

The inspected tstack README and skills do not establish that Theo compiled his workflows from Matt and Poteto. Similarities support a comparison, not attribution of influence. No video or social-post transcript establishing that lineage was verified. The recommendations below are grounded in the linked files rather than invented quotations from videos.

## Comparison

| Dimension | Matt Pocock | Poteto | Theo / T3 Code | Factory choice |
| --- | --- | --- | --- | --- |
| Organizing skills | Strong invocation boundaries and precise pointers; current catalog is much broader than one tiny grill skill | Persistent knowledge, principles, planning and review skills, plus scoped verification maps | A small task-oriented skill set with explicit dependencies and native-tool fallbacks | Six substantial capabilities; one orchestrator owns sequence |
| Managing context | Separate always-loaded pointers from conditional detail; delete duplicate meanings and no-op instructions | Load domain knowledge and keep memory pruned; feature maps let verification load one area | Personal model settings live in project instructions; internal docs carry hard-to-discover reasons | Keep specialized references conditional; avoid a new memory system |
| Defining work | Grilling follows prerequisite decisions and separates researchable facts from user decisions | Medium/large plans define scope, alternatives, phases and proof | Understand intent and choose the smallest coherent change; modernize the idea as well as the branch | Short living spec, with alternatives only for consequential choices |
| Reviewing | Current catalog separates standards and spec review; agent-writing guidance emphasizes checkable completion | Principle-grounded review across scope, architecture, code, tests and performance | Verify findings, defend scope, prefer narrow fixes, review changed behavior in bounded rounds | Evidence-based spec and implementation review, optional council |
| Proving work | Completion criteria should be clear and demanding enough to prevent premature completion | “It compiles” is insufficient; drive real entry points and preserve evidence | Directly observed proof; focused tests at the right layer and real UI/runtime evidence | Keep tests, review, rendered acceptance and product outcome distinct |
| Learning | Prune stale instructions and use the environment as source of truth | Encode recurring lessons in tools, types, lint and boundaries; memory pruning is explicit | Prefer enforceable project checks and avoid redundant docs or tests | Retain Factory helpers/evaluations; add prose only for judgment |
| Autonomy | Grilling is deliberately an interview that waits for user decisions | Plan/review skills deliberately stop at their deliverable and can require structured interaction | Full-send and full-stop carry different explicit authorization boundaries | Honor the requested destination; no universal confirmation stage |

Matt's current `grill-me` is a thin router, so “all thin skills are bad” would misrepresent his approach. A wrapper can earn its place through a distinct invocation boundary. Factory's old capability splits mostly repeated workflow steps without that benefit. Similarly, Poteto's more prescriptive planning is a deliberate workflow choice, not a universal requirement we must copy.

## Theo's actionable guidance

These are paraphrases tied to primary sources. They are defaults with context, not external regulations.

### Keep the model small

[T3 Code: A note from Theo](https://github.com/pingdotgg/t3code/blob/316c3256a3a09cef7ed68914ebe74c7183ac08e1/AGENTS.md#a-note-from-theo) favors ambitious outcomes and simple systems, removing inherited complexity and resisting impressive but unnecessary machinery. His instruction combines thoughtful preparation with avoiding speculative work.

**Adopt:** collapse capabilities that agents can already perform together; keep the recursive behavior in one place. **Avoid:** an agent role per skill, a new scheduler, a generic workflow framework, and preserving empty wrappers solely to keep the old directory tree.

### Protect the intended scope throughout review

[sol-loop](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/sol-loop/SKILL.md) asks for the smallest useful corrections and explicitly permits disagreement with reviewers. It distinguishes defects in the intended case from optional nits, keeps stable finding IDs and dispositions, and narrows later rounds to changes and open findings. [babysit-pr](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/babysit-pr/SKILL.md) applies the same discipline to bot feedback.

**Adopt:** independently validate findings, fix real in-scope defects, reject false positives with evidence, retain optional work as follow-ups. **Avoid:** adding guards, compatibility, abstractions or tests just because a reviewer can imagine them. Scope discipline must not become an excuse to dismiss an actual introduced defect.

### Bound iteration without manufacturing success

Sol-loop defaults to three rounds, with limited extension for specified high-risk cases or user direction. An unresolved dispute or expired budget is not agreement. Its named-model requirement is strict: unavailable Sol is reported, not silently replaced.

**Adopt:** bounded rounds and explicit unresolved states. **Adapt:** Factory uses three review passes per cycle, two outer returns, and an earlier no-progress stop. The outer limit is our design, not Theo's. Factory's generic review can use available models; an explicitly named reviewer or requested three-provider council cannot be silently substituted.

### Use independent perspectives honestly

[council](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/council/SKILL.md) calls for three strong models from different providers, read-only reviews, fresh review after fixes, no concurrent edits to the reviewed checkout, and explicit reporting of unavailable providers. It asks for scores and forbids invented ones.

**Adopt:** independent briefs, stable snapshots, real capability discovery, synthesis of agreements and disagreements, and honest reviewer identities. **Adapt:** council is optional; Factory does not require paid multi-provider review for every small fix. Findings and proof govern acceptance, not average scores. Council's own continue-until-satisfied instruction is bounded in Factory using the anti-churn reasoning from sol-loop.

### Proof must cover what the user will experience

[full-send](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/full-send/SKILL.md) requires observed command output, reproduction, screenshots or similar proof. Green mocked tests do not establish the actual user experience. [T3 Code's verification guidance](https://github.com/pingdotgg/t3code/blob/316c3256a3a09cef7ed68914ebe74c7183ac08e1/AGENTS.md#verifying) focuses tests at the lowest meaningful layer, extends existing cases, and avoids tests of trivial wiring or what types already guarantee. Visual fixes can use before/after captures.

**Adopt:** cheapest credible proof, real consumer paths, and focused regression protection. **Avoid:** universal test quotas or duplicating the same behavior at every layer. Factory keeps its stronger existing rendered-interface gate, including assets and motion. Project-required checks still apply.

### Delivery permission is specific

[full-stop](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/full-stop/SKILL.md) explicitly stops before merge; full-send explicitly authorizes merge once its gate passes. Those are invoked workflows, not permissions inherited merely by reading a skill.

**Adopt:** distinguish branch, PR, merge and deployment destinations. **Avoid:** importing full-send's merge/force-push grants into ordinary Factory work. The user asked for this redesign on a branch; integration and publication as a release remain separate.

### Review the current content and target

Sol-loop fixes its comparison base; full-send's merge gate applies to the latest commit. Babysit-pr checks changed base state and fresh CI. A green check or review on an earlier patch is not current acceptance.

**Adopt:** retain Factory's existing revision fingerprint and delivery guards. Their machine checks are more reliable than another reminder paragraph. Keep useful old reasoning as context, but refresh receipts and affected checks when content or target changes.

### Preserve intent and ownership when changing structure

[modernize](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/modernize/SKILL.md) asks whether a PR still belongs, not merely whether it rebases. [takeover](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/takeover/SKILL.md) treats inherited work as context, preserves authorship, and rechecks the original failure.

**Adopt:** inspect the previous implementation and keep useful behavior rather than defending every file. Factory retains design expertise, evidence contracts, safety guards and historical evaluation receipts while replacing the old routing structure.

### Keep documentation and communication useful

[file-pr](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/file-pr/SKILL.md) leads with the problem and resulting behavior, rather than a file inventory. T3 Code's [documentation guidance](https://github.com/pingdotgg/t3code/blob/316c3256a3a09cef7ed68914ebe74c7183ac08e1/AGENTS.md#documentation) reserves internal docs for rationale and constraints that source does not reveal. Its working plans and research notes are normally temporary.

**Adopt:** concise handoff, actual proof, useful limitations, one authoritative place per rule. **Adapt:** this research/rationale and migration guide are retained because the requested redesign needs reviewable provenance and intentionally changes public skill names. Routine execution plans are not new permanent documentation. [leaving-pr-comments](https://github.com/t3dotgg/tstack/blob/11e37a74d0a6868c121cd0910ab2b3bd9873b92a/skills/leaving-pr-comments/SKILL.md) informs attribution, but reading it does not authorize sending comments.

## Selective contributions from Matt and Poteto

[Matt's writing-for-agents](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md) is the strongest basis for pruning: precise triggers, progressive disclosure, co-located concepts, single sources of truth, and removal of instructions the model already follows. We keep checkable completion criteria without imposing the same headings on every skill. [Grilling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) contributes the distinction between facts an agent should find and decisions the user owns; its exhaustive interview and explicit confirmation are not appropriate defaults for this already-authorized refactor.

Poteto's [plan](https://github.com/poteto/brainmaxxing/blob/ec4d8e43dee639d6f5d94aed3ca16af7b298ecfc/.agents/skills/plan/SKILL.md) and [review](https://github.com/poteto/brainmaxxing/blob/ec4d8e43dee639d6f5d94aed3ca16af7b298ecfc/.agents/skills/review/SKILL.md) contribute explicit proof, architectural alternatives and severity-aware critique. We omit mandatory task-tool rituals, file-count thresholds, fixed phase sizing, automatic skill installation, and asking the user to choose among several options for every review finding.

[Encode lessons in structure](https://github.com/poteto/brainmaxxing/blob/ec4d8e43dee639d6f5d94aed3ca16af7b298ecfc/brain/principles/encode-lessons-in-structure.md) and [subtract before you add](https://github.com/poteto/brainmaxxing/blob/ec4d8e43dee639d6f5d94aed3ca16af7b298ecfc/brain/principles/subtract-before-you-add.md) reinforce retaining tested helpers and deleting generic prompt scaffolding. Her verification example supports narrow feature-level references with launch/health/interaction/evidence/cleanup. It is explicitly fictional and omits the driver; Factory does not claim its sample commands are working tooling.

## Design decisions this research supports

One orchestrator owns the two inner loops and bounded outer return. Spec combines discovery, requirements, codebase research and architecture. Design combines shaping, translation, inspection and interface acceptance. Review challenges both specs and implementations. Verify joins deterministic testing and product validation without conflating their verdicts. Deliver joins repository workflow and release while preserving authorization boundaries.

This preserves Factory's useful behavior while reducing its discovery and maintenance surface. It is a branch candidate for evaluation, not evidence that shorter instructions automatically perform better. See [migration](migration-v3.md) and [evaluations](../evaluations/README.md).
