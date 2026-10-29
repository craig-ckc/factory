# Remaining tasks: implementation and acceptance

Source: the six tasks supplied on 2026-10-29. Baseline: [Factory 2.1.1, 647d6b0](https://github.com/craig-ckc/factory/commit/647d6b0885caf7c3e47f907a7898daf07ac2090f). Living scope, implementation PR, exact reviewed/merged revisions and final post-merge acceptance: [issue #1](https://github.com/craig-ckc/factory/issues/1). Candidate: 2.2.0. This source record describes the implementation and reproducible evidence; delivery receipts live in the issue/PR so they can name this commit without a self-referential documentation commit.

## 1. Project verification and local CI

Already present: Testing's local-check guidance and Product Validation's project flow. Added: advisory discovery, explicit verification contracts, bounded execution/evidence/cleanup, portable project-skill generation, and conditional verification guidance. Factory's own contract is `.factory/verification.json`. No discovered command is automatically executed. CI matrix jobs are locally runnable Python checks; other OS results require the corresponding runner.

Evidence: 23 verification helper tests exercise successful/failed interaction, readiness, timeouts, always-attempted teardown, no-shell execution, evidence preservation and source identity. The generated Factory project skill passes the Skill Creator validator. Advisory discovery was exercised against the existing Preflight monorepo, finding root/workspace scripts without executing them. Factory's actual CLI contract and exact-revision local checks are part of the PR acceptance record. Windows exited-leader descendant cleanup remains explicitly INCONCLUSIVE.

## 2. Delivery and branch safety

Already present: safe integration policies. Added: precise checkpoint/acceptance/stacked-merge guidance and read-only fingerprint, acceptance and cleanup guards. Exact head/target/merge-base/diff bind acceptance; dirty, active, dependent, advanced, protected and unknown-ownership branches are retained. Squash proof is explicit; uncertain rebase integration stays blocked.

Evidence: 22 temporary Git/bare-remote tests exercise stale head/target, dirty/untracked work, active worktrees, unresolved dependencies, useful commits, advanced remote tips, normal integration, attributed squash proof, and raw-SHA/tag self-proof refusal. The actual implementation PR supplies hosted checks, independent exact-patch review, merge, original-main synchronization, safe cleanup and retained discussion/diff evidence in the linked issue. The guard cannot authenticate caller-supplied GitHub metadata or guarantee a later mutation is race-free.

## 3. Learning and evaluation

Added: conditional evidence-based learning guidance, packaging checks, meaningful helper tests, fixed behavioral requests/rubric and content-bound baseline/candidate comparison receipts. The initial repository has no review/revert history establishing recurrence; version drift, stale acceptance and unsafe cleanup are explicitly seeded failure classes.

Evidence: executable packaging regressions reject manifest version drift, wrong sources and broken references. Eight comparison tests reject changed output/requests, missing or duplicate cases, an empty task set, a candidate regression and INCONCLUSIVE promotion. Independent review of this change found two instances of accepting insufficient proof (a topic's own SHA and an empty evaluation set); both were reproduced and converted to passing negative regression tests. A separate lifecycle finding became a teardown regression. These review findings are actual change history, distinct from the initially seeded cases. The paired behavioral outputs, hashes and independent decisions are in [evaluation results](../evaluations/results/). No claim of universal reliability follows from this small task set.

## 4. Discovery and requirements

Already implemented in product-discovery, requirements, codebase-research and architecture. No rewrite is warranted. Separate baseline/candidate agents performed the same unclear-feature task using supplied facts, explicit assumptions, outcome evidence and traceable scope reasoning; a different evaluator applies the maintained rubric. Supplied scenario notes are not user interviews or measured research. See the retained outputs and comparison receipts.

## 5. Independent responsibilities and outcome acceptance

Already implemented in testing, code-review, interface-review and product-validation. Added reusable verification linkage. Both behavioral runs executed the invoice CLI and tests: the paid-report test passes, while the original outstanding-report outcome fails (paid A/100 instead of outstanding B/C/75). A separate evaluator independently reproduced that mismatch. Retained subprocess records are evidence artifacts, not signed historical transcripts. The implementation itself receives independent exact-patch review in the PR. The CLI scenario does not establish visual-interface acceptance; this change adds no visual UI.

## 6. Delivery, adoption and compatibility

Mechanics remain in GitHub Workflow/Release and their shared reference. The actual PR delivery receipt names checks/review/merge, original checkout synchronization, cleanup and retained PR evidence. [Compatibility evidence](../evaluations/results/compatibility.json) records native Codex discovery of all 17 candidate skill paths without parse errors, all 17 skill validations and valid Claude marketplace/plugin manifests. Full Claude model behavior is INCONCLUSIVE because the CLI is logged out; Cursor runtime is INCONCLUSIVE because Cursor is absent. Structural compatibility passes. Deployment is N/A for this repository. These unavailable model-runtime contexts remain a coverage gap rather than an invented PASS, and global installations are not promoted by this repository update.

## Version notes

The implementation PR/Git diff provides complete before/after skill bodies against the immutable baseline; this record avoids duplicating those bodies. New tooling is additive. Marketplace identity and the existing seventeen skill names remain compatible; plugin versions advance together to 2.2.0. Global installed copies are outside this repository change's scope.
