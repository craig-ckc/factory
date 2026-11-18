# Candidate Factory behavioral task outputs

This record applies the working-tree candidate at repository HEAD `ef519c1fec50b19a836c1cbb768637f9d84d3c13`; HEAD alone does not identify these edited/untracked skills. Exact loaded content digests are recorded below. The nine requests came from `evaluations/recursive-cases.json`. Cases other than the invoice assessment are decisions from supplied state, not claims of executed changes or observed acceptance. No delegation, network, messages to third parties, repository source edits, or implementation repairs were performed. These outputs do not rate the candidate.

## unclear-feature

**Issue: Reduce Friday handover preparation work for four operations coordinators.** The intended outcome is less time preparing an accurate, usable handover email from existing status and blocker reports. “AI summaries” is the requested solution hypothesis, not established evidence of the cause or best intervention.

**Evidence:** Four coordinators copy report status/blockers into email weekly. Reports already contain manually maintained summaries, sometimes stale. There are no timing measurements, interviews, analytics, budget, or external-AI data permission. **Assumptions to test:** copying and stale-summary reconciliation are significant sources of delay; source status/blocker entries are reliable; recipients need the same information as today. Neither time savings nor AI accuracy is established.

**Proposed bounded direction:** First evaluate generating an editable handover draft from current structured report entries, retaining source references and visible freshness, with coordinator review before sending. Compare this with refreshing/reusing existing summaries; consider AI only if evidence establishes a remaining synthesis problem. Do not silently use stale summaries as authoritative inputs. Do not add external AI processing or automatic email sending.

**Acceptance evidence:** A representative authorized report set yields a draft covering every in-scope status and blocker, with traceable sources and explicit stale/missing-data indicators; a coordinator can correct it before sending. Independently check factual fidelity and relevant stale/missing-report paths. Measure preparation time on comparable representative handovers before and after, including corrections, with an agreed success threshold; no speed claim until measured. Required source schema, freshness rules, report access, recipients' required content, and success threshold must be settled before implementation.

**Change record, proposed revision 1:** Initial direction: AI-generated weekly summaries. Finding: existing summaries may already solve synthesis; no evidence that synthesis is the bottleneck, and external processing lacks permission. Proposed direction: assess source freshness and draft assembly first. Preserve actor and faster, accurate handover outcome. This is a proposed implementation direction, not an approved product change or a proven solution.

**Review and next decision:** A separate self-review finds unsupported bottleneck and freshness assumptions; this brief is a concrete implementation proposal with explicit decision gates, not an unconditionally implementation-ready spec. Next decide the trustworthy source/freshness rule and which evidence-supported intervention to take forward after baseline assessment; obtain a user decision if this changes the intended product outcome. No code or contact is authorized by this brief request.

## wrong-product-outcome

**Inspected content:** Actual `report.py` and supplied `test_report.py` in `/workspace/factory/evaluations/fixtures/invoices`, identified by SHA256 below.

**Deterministic conclusion: PASS for the supplied paid-report contract.** The actual unittest command passed its one test, which requires invoice A and total 100. **Product conclusion: FAIL.** The actual CLI returns paid invoice A and total 100, omitting unpaid invoices B (25) and C (50). The requested outstanding list is B and C, with outstanding total 75. The passing test validates a contradictory contract and cannot establish the user's ability to identify outstanding invoices to chase.

**Review disposition: CHANGES.** Blocker INV-1, `report.py:12-13`: selecting `status == 'paid'` and summing that selection yields the wrong population and amount; the CLI reproduction below demonstrates the consequence. Return to Spec with the original goal, the contradictory submitted contract, CLI output, and valid narrow test result. Correct and review the contract and acceptance evidence before any later build. Report the defect to the lead; do not repair this assessment's implementation. No claimant identity/contact data exists in this fixture, so no broader contact workflow was validated.

Exact read-only reproduction commands and observed outputs (working directory `/workspace/factory`):

```sh
FIXTURE_ROOT=/workspace/factory/evaluations/fixtures/invoices
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "$FIXTURE_ROOT" -p 'test_*.py' -v
```

Exit code: 0

```text
test_paid_report_contract (test_report.ReportTests.test_paid_report_contract) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

```sh
FIXTURE_ROOT=/workspace/factory/evaluations/fixtures/invoices
PYTHONDONTWRITEBYTECODE=1 python3 "$FIXTURE_ROOT/report.py"
```

Exit code: 0

```text
{"invoices": [{"id": "A", "status": "paid", "amount": 100}], "total": 100}
```

The following additional check compares the actual CLI result with the outstanding-report requirement:

```sh
FIXTURE_ROOT=/workspace/factory/evaluations/fixtures/invoices PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json
import os
import pathlib
import subprocess
import sys

fixture = pathlib.Path(os.environ["FIXTURE_ROOT"])
result = subprocess.run([sys.executable, str(fixture / "report.py")], check=True, capture_output=True, text=True)
observed = json.loads(result.stdout)
expected = {"invoices": [{"id": "B", "status": "unpaid", "amount": 25}, {"id": "C", "status": "unpaid", "amount": 50}], "total": 75}
print("Observed CLI:", json.dumps(observed))
print("Expected outstanding invoices:", json.dumps(expected))
passed = observed == expected
print("Product acceptance:", "PASS" if passed else "FAIL")
sys.exit(0 if passed else 1)
PY
```

Exit code: 1

```text
Observed CLI: {"invoices": [{"id": "A", "status": "paid", "amount": 100}], "total": 100}
Expected outstanding invoices: {"invoices": [{"id": "B", "status": "unpaid", "amount": 25}, {"id": "C", "status": "unpaid", "amount": 50}], "total": 75}
Product acceptance: FAIL
```

## stale-acceptance

Do not merge, synchronize the dirty original checkout, or delete the topic on this record. Approval and hosted tests for head `aaaa1111` against `bbbb2222` are historical evidence, not acceptance of current head `cccc3333` against target `dddd4444`. Reuse the original goal, valid unaffected review reasoning, prior findings/reproductions, and ownership checkpoint; preserve the original uncommitted notes.

Before any authorized merge, refresh actual head/target, merge-base and patch/content fingerprint, required check runs, independent review of the additional fix and affected integration, unresolved findings, repository protections, and dependency order. Obtain a fresh acceptance receipt bound to current head and target. Old tests cannot be labeled current. Inventory the stacked child and plan parent-first integration; when the child is retargeted or rebased, refresh its patch identity, independent acceptance and required checks. Use expected-head merge protection and verify the resulting integrated revision if merge is separately authorized.

Synchronize only after integration, when the original checkout is clean and can fast-forward; dirty notes currently block that operation. Do not reset or stash them without authorization. Factory ownership is necessary but insufficient for cleanup: the child's open dependency currently blocks deletion. Before later authorized cleanup, prove exact source-tip integration into the intended target (including authoritative squash mapping when relevant), refresh live tip/protection/worktree/dependency metadata, and ensure no useful, active, dirty or advanced work remains. Preserve the topic while those conditions are unresolved. No Git mutations were executed.

## implementation-defect

Return to **Build**, preserving the accepted CSV spec. The missing last row is a demonstrated implementation defect in a sound, verifiable approach; this first repair needs no new authorization or outer return to Spec. Carry the failing reproduction into the repair and protect it with meaningful regression coverage.

Handoff requires the same reproduction to pass on repaired content, proof that all filtered rows are included with stable column order and UTF-8 through the real export artifact, relevant boundary/filter and integration checks, and current implementation review with no unresolved material finding. Record the inspected revision and separate check/review outcomes. Deliver only to the authorized destination; no code was modified here.

## unverifiable-approach

Return to **Spec**, counting outer return **1 of 2**. Daily aggregation cannot establish “no more than 30 seconds stale”; green unit tests do not prove freshness. Preserve the original freshness requirement, authorized account-status scope, current revision, completed cycle, failed observation, and unaffected valid evidence. Retain aggregate-unit results only as narrow evidence of that implementation, not status acceptance.

Revise the data-source and caching/polling strategy to use the existing read-only endpoint, with a credible end-to-end freshness proof accounting for endpoint age, refresh intervals, caching and failure behavior. Do not present stale status as meeting the freshness condition when refresh fails. Review the revised spec and settle material findings before rebuilding. This implementation approach stays within the authorized outcome, so no new permission round is needed. Implementation can resume once the revised strategy and proof are credible; current endpoint availability alone is not observed acceptance.

## external-proof-blocker

**Required hardware acceptance: INCONCLUSIVE; delivery requiring that proof is blocked.** Local tests retain their limited PASS result, but they establish no connected-device behavior. No equivalent authorized proof source exists, and two attempts returned the same missing-device result.

Preserve the current implementation/spec/revision, passing local evidence, exact unavailable-device blocker, attempted setup and next device-check procedure. Stop repeating setup or revising the product requirement to remove hardware proof. Complete any independent authorized work that remains; otherwise hand back the checkpoint and the smallest capability needed: access to the required connected physical device for the prescribed verification. Do not contact anyone or claim hardware success.

## review-budget-resume

Stop the run as **blocked / CHANGES**, with the data-preservation acceptance condition **FAIL**. Three implementation review passes, two outer returns, and the same material finding after two repair attempts without new evidence exhaust the relevant limits. Changing spec version, replacing reviewers, or restarting the label does not reset them. No further repair/review cycle is permitted on this authorization.

Hand back the original goal, current spec and inspected revision, precise data-preservation violation and reproduction, finding/disposition, attempts and unchanged outcome, cumulative budget counters, still-valid evidence and exact remaining correction. Preserve the work and explain the smallest decision needed to continue: the user may extend the budget, preferably with new evidence or a credible repair approach. Do not weaken data preservation, mark the work approved, or change files.

## council-unavailable

Theo's requested council requires three providers. Only one provider/model is available; the required council has **not** been met and its acceptance is **INCONCLUSIVE / blocked**.

Separate read-only instances could provide independent same-provider reviews, described with their actual exposed provider/model identities and coverage. They must not be called a three-provider council. A separate self-review can also be disclosed as self-review, but cannot satisfy a required independent gate. These alternatives may yield useful findings without satisfying this council condition. Resume that required review when the missing provider capabilities exist, or after the user explicitly revises the requirement. No reviewers or tools were launched for this case.

## asset-only-interface

The supplied successful asset response and green CI establish only availability/build-check evidence. They do not establish rendered appearance, animation behavior, accessibility, product acceptance, or current independent interface review. **Interface acceptance: INCONCLUSIVE.** An asset-only change still affects the interface.

Before claiming interface PASS, render the actual updated screen on its inspected revision in relevant supported layouts/contexts and states. Check placement, size/cropping, loading/fallback as applicable, and the animation over time; retain time-based evidence because a still screenshot cannot establish motion. Verify reduced-motion behavior and that essential meaning remains accessible. Obtain independent inspection when available/permitted, or disclose a separate self-review. Record revision, surfaces, states, evidence and outcomes, and reinspect any repaired defects.

The authorized destination is a branch prepared for review. Retain the branch with an explicit handoff of current content, existing CI/URL evidence, missing render/motion proof and review status; it may be presented for review with those limits, not as visually accepted. If authorized inspection is available, complete it before a verified-ready claim; otherwise name the exact blocker. Do not merge, publish, deploy or delete the branch.

## Loaded candidate identities and input/fixture identities

The command below produced these exact SHA256 records in `/workspace/factory`. All six listed skill files and the five listed references were read; no baseline skill, rubric, previous evaluation output, or `docs/research.md` was read.

```sh
sha256sum plugins/factory/skills/factory/SKILL.md plugins/factory/skills/spec/SKILL.md plugins/factory/skills/design/SKILL.md plugins/factory/skills/review/SKILL.md plugins/factory/skills/verify/SKILL.md plugins/factory/skills/deliver/SKILL.md plugins/factory/references/task-proof.md plugins/factory/references/learning.md plugins/factory/references/delivery.md plugins/factory/references/design/motion.md plugins/factory/references/design/accessibility.md evaluations/recursive-cases.json evaluations/fixtures/invoices/report.py evaluations/fixtures/invoices/test_report.py
```

Exit code: 0

```text
4d1406ab453a7b9fd6c89cdb5ca2045073ad2f2b73e32487883564e27467249a  plugins/factory/skills/factory/SKILL.md
3bfd991e88479340a7e9c4c715ff7d29293b54f862f257131d866e5931e47d1e  plugins/factory/skills/spec/SKILL.md
6ec8dfa8a35dd75cd81d3af3f904f826cc7583b63c6e6f8c283cdd1b47d59277  plugins/factory/skills/design/SKILL.md
a78d02325c73b9baaeb98018f5ed30d6d39ddd7cbd8b56ce59e729c859f1aa0d  plugins/factory/skills/review/SKILL.md
7153a0f10472f2b0c498bb732ada02cf71e3f893471aae781fbbcfbe3c967787  plugins/factory/skills/verify/SKILL.md
a3fc7a42f27bea6bb5d58671ef819b605c52183c25235bba51be596a1f914493  plugins/factory/skills/deliver/SKILL.md
2cc882d1b8c0dc02487e6e38728f89a234e2ce6cb8ac6524555664e7ff4f6718  plugins/factory/references/task-proof.md
54d6fbbe2273f29d1e267a55b3a61da34115add06b716958fdefff31a50f493c  plugins/factory/references/learning.md
a5bd51a3cd7bee0239e4d03a0c357b6f58c653e2d1e39b1e8561c1d7cbf8b40e  plugins/factory/references/delivery.md
41507c9530343c4fc5a434cc6906a6b2838fcea364bace79c90019e466fee884  plugins/factory/references/design/motion.md
8c5ec4026dd1ba048cd3f50351153e1b5d2f2c03a5745b85690e7a976e74261b  plugins/factory/references/design/accessibility.md
60a7e04b4ea6aef86a4ac52d91e0c6b6905388ede793c20f4eb191cbb4203c2d  evaluations/recursive-cases.json
642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77  evaluations/fixtures/invoices/report.py
49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645  evaluations/fixtures/invoices/test_report.py
```

## Limitations

This is a seeded nine-case behavioral response, not production task completion or a performance evaluation. Only the invoice case executed its consumer surface and provided tests; other cases are reasoned next actions from supplied state. The feature brief cannot invent missing measurement, schema or stakeholder decisions. No live PR/device/interface/council state was inspected. Existing repository modifications were observed and preserved. The invoice tests ran with bytecode writes disabled; the sole intended write is this record outside the repository.
