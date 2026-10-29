# Candidate Factory task responses

Performed on 2026-10-29. Skills were read exclusively from `/Users/Craig/Developer/Projects/factory/plugins/factory/skills` and their linked references in the same candidate plugin. No rubric, baseline definitions, other evaluator output, or comparison receipt was read. No Git or external mutation was executed. The invoice fixture was inspected and executed without repair; Python bytecode writes were disabled. This file is the only written artifact.

## unclear-feature

### Task response: issue-style implementation brief

**Title:** Reduce Friday handover preparation time while preserving current status and blockers.

**Actor and outcome.** Four operations coordinators prepare the Friday handover email. The intended improvement is less coordinator time spent preparing and checking a useful, accurate handover. “Add AI summaries” is a proposed means, not the acceptance condition.

**Evidence.** The supplied stakeholder note says the coordinators copy status and blockers from existing reports into an email each Friday. Those reports already have manually maintained summaries that are sometimes stale. This is reported stakeholder context, not direct workflow observation or measured timing. No report samples, repository, schemas, interviews, analytics, timing measurements, budget, or authorization to send data to an external AI service were supplied.

**Hypotheses, not findings.** Copying may be the main time cost; checking stale summaries may instead dominate. A generated summary may reduce reading time, but it could repeat stale material or add correction work. Existing status and blocker fields may be sufficient to assemble the email without generation. Their structure and freshness are unknown. We cannot yet claim AI is necessary, that any approach saves time, or that the available reports are authoritative for the current week.

**Smallest decisive uncertainty.** Is the avoidable effort primarily transferring existing current information, or interpreting and correcting it? Before committing to a production approach, obtain an authorized, locally reviewed example of a completed Friday handover and its source reports; record preparation, checking, and correction time and the source of stale content. This is a proposed next activity, not research already conducted. No contact or data collection was performed here.

**Recommended first slice, conditional on that decision:** a local draft compiler that assembles current status and blockers from the existing reports into the established email structure, with source references and explicit freshness/unknown warnings, followed by coordinator review. Preserve the current sending workflow. Do not feed stale manual summaries into a generator and assume they have become current. If interpretation rather than copying is the bottleneck, revisit this slice before Build.

**Issue change record.**

| Field | Recorded decision |
| --- | --- |
| Original request | Add AI summaries because weekly handover takes too long. |
| Evidence changing direction | The reports already contain summaries, some stale; coordinators also copy existing status and blockers. There is no measured bottleneck or external data permission. |
| Proposed direction | Validate the time/freshness bottleneck, then prefer a bounded local draft compiler if copying is the bottleneck. Defer AI/provider selection. |
| Rationale | Generation does not establish freshness and may add review effort. A deterministic draft can reuse existing information with a smaller data and operational boundary. |
| Preserved product intent | Reduce coordinator handover preparation effort while keeping the handover accurate and useful. |
| Decision status | Recommendation awaiting evidence and selection of the first slice; no claim that stakeholders approved it. If the desired product outcome changes, obtain explicit approval and update this record. |

**Behavioral contract for the proposed compiler slice.**

1. A coordinator selects the intended week and report set and requests a draft. Match the existing report and email conventions once inspected; do not invent a new permanent workflow.
2. Include each selected report's available status and blockers once, retaining source identity/reference and the source's available update timestamp. Keep source text attributable; omit no blocker silently and invent no status, owner, date, or action.
3. A missing status, missing blocker field, missing timestamp, unavailable report, or freshness concern is explicit in the draft/diagnostics. Missing data is not equivalent to “no blockers.” Freshness thresholds and the authoritative source must be agreed before implementing that rule; do not infer that “recently read” means “recently updated.”
4. The coordinator can review and correct the draft before using the existing email process. No automatic send, write-back to reports, model call, external upload, or new credentials belongs to this slice.
5. Restrict input access to reports the coordinator is already allowed to read. Keep processing local and avoid retaining report content in diagnostics beyond existing authorized storage. Reuse the existing identity and permission boundary once discovered.
6. Re-running unchanged selected inputs produces equivalent content and ordering under the established email convention. A source change must be reflected on regeneration; a saved draft must not imply that its sources are still current.

**Boundaries and architecture.** No handover codebase was provided, so no entry point, module, integration, deployment dependency, or existing permission implementation has been verified. Do not name invented files or assert compatibility. Before Build, trace the real report read path, email preparation path, freshness metadata, permissions, and tests. Prefer a small compiler inside that existing flow: permitted report reader → normalized current fields plus source metadata → deterministic draft formatter → human review. The source reader owns access and availability errors; the formatter must not silently turn unavailable data into an empty successful handover. Keep any future summarizer behind an explicit boundary with provenance and the same missing-data semantics. A model/provider choice would have lasting data and operational consequences and needs a separate decision supported by necessity, budget, and data authorization.

**Acceptance evidence, defined before implementation.**

| Claim | Evidence required |
| --- | --- |
| Correct compilation | Local tests using approved representative examples: expected report set, statuses and blockers retained exactly once, source attribution, stable ordering, and source updates reflected on regeneration. |
| Honest failure/freshness behavior | Tests and a real coordinator flow for stale/unknown timestamps, missing report/field, and denied access; no fabricated “all clear” or silent omission. Agree the freshness rule first. |
| Fits the real workflow | Observe a coordinator prepare and review the draft using the actual product surface and established email format; obtain interface review for the implemented experience. No such review has occurred yet. |
| Saves effort without shifting it | Compare the full preparation + review + correction time with a measured baseline on comparable Friday packets. Agree a meaningful reduction threshold before the trial. The four-coordinator population is known; no numeric success target or measured saving is invented here. |
| Remains useful and accurate | Coordinator checks current status/blockers against authoritative sources and records omissions, stale claims, and corrections; the acceptance sample must contain no unflagged material omission or unsupported claim. |
| Respects data boundary | Verify no external service request or unauthorized report access and no automatic email send in the slice. |

**Next decision.** Authorize the smallest local workflow/baseline examination and choose whether the first build should address copying, source freshness, or interpretation. The immediate decision is not which AI model to buy. Before production Build, resolve authoritative fields and freshness policy, inspect the actual source/software boundary, agree the measurable success threshold, and independently challenge the resulting spec. This is an implementation brief with explicit readiness gates, not a claim that a missing codebase and unmeasured outcome have already been resolved. No code was implemented and nobody was contacted.

### Evidence and limits

Applied Product Discovery, Requirements, Codebase Research, and Architecture. The stakeholder note in `cases.json` is the only domain evidence. No codebase for the handover was supplied or inspected. The architectural flow and compiler behavior above are proposed contracts, not descriptions of existing software. This is an author assessment; independent specification review was not performed in this case.

## wrong-product-outcome

### Task response: independent assessment

**Do not accept this change for the original request.** The provided deterministic test passes for the submitted paid-invoice contract. The actual CLI fails the original outstanding-invoice outcome. I did not author or repair the submitted implementation.

Inspected content is the two files in `/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices`, identified by these SHA-256 hashes, verified again after execution:

| File | SHA-256 |
| --- | --- |
| `report.py` | `642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77` |
| `test_report.py` | `49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645` |

No PR diff, submitted commit SHA, previous implementation, or hosted CI metadata was provided. The verdict applies to this inspected file snapshot, not to an assumed Git revision or unseen diff.

| Assessment | Verdict and scope |
| --- | --- |
| Deterministic testing | **PASS** for the one provided test and supplied paid-report contract: A is listed and the total is 100. The test process exits 0. This is not evidence of outstanding-report acceptance or broad edge-case coverage. |
| Code review | **FAIL / approval withheld** against the original objective. `report.py:12–13` filters `paid` and totals that same set, excluding outstanding invoices. The narrow paid-contract implementation is consistent with its test, but its contract conflicts with the user request. No other material finding is asserted from an unseen diff. |
| Interface review | **FAIL** for the inspected CLI response's requested behavior: it presents paid A and 100 where outstanding B/C and 75 are required. The terminal JSON is the actual observed interface. No graphical, interactive, accessibility, or other platform state was supplied or approved. |
| Original product outcome | **FAIL.** The user cannot use this report to identify the supplied outstanding invoices or their outstanding total. A separate check consuming the real CLI exits 1. |

**Finding [P1]: wrong invoice population and total.** At `report.py:12`, the paid filter selects A (100), while the fixture's unpaid invoices are B (25) and C (50). Line 13 consequently reports total 100 instead of outstanding total 75. The supplied assertion at `test_report.py:7–10` enforces that conflicting paid-report contract. Reproduce with `python3 report.py` in the fixture root: the CLI returns A/100. Return the material contract mismatch to Requirements, reconcile it with the original outstanding-invoice purpose, then have Build update the implementation and regression protection and obtain fresh review/product validation. No repair was made here.

### Commands and results

All commands below ran in:

```text
/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices
```

The source was read with line numbers using Python (`Path.read_bytes()`, SHA-256, and `enumerate(...splitlines(), 1)`). No ancestor `AGENTS.md` was found by checking the fixture directory and each ancestor. Fixture inventory with `rg --files -g '!__pycache__/**'` returned only `report.py` and `test_report.py`.

Provided tests:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v
```

```text
test_paid_report_contract (test_report.ReportTests.test_paid_report_contract) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Exit status: **0**.

Real CLI:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 report.py
```

```json
{"invoices": [{"id": "A", "status": "paid", "amount": 100}], "total": 100}
```

Exit status: **0**. A successful process exit does not establish the requested product result.

Original-outcome check through the actual CLI; this script was passed on stdin and not saved to the fixture:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json
from pathlib import Path
import hashlib
import subprocess
import sys
proc = subprocess.run([sys.executable, 'report.py'], text=True, capture_output=True, check=False)
print(f'CLI exit: {proc.returncode}')
if proc.stderr:
    print(proc.stderr, end='')
if proc.returncode:
    sys.exit(proc.returncode)
actual = json.loads(proc.stdout)
expected_ids = ['B', 'C']
expected_total = 75
actual_ids = [row['id'] for row in actual['invoices']]
print(f'Expected outstanding IDs: {expected_ids}; actual IDs: {actual_ids}')
print(f'Expected outstanding total: {expected_total}; actual total: {actual["total"]}')
for name in ['report.py', 'test_report.py']:
    p = Path(name)
    print(f'SHA256 {name}: {hashlib.sha256(p.read_bytes()).hexdigest()}')
passed = actual_ids == expected_ids and actual['total'] == expected_total
print('Original-outcome CLI check: ' + ('PASS' if passed else 'FAIL'))
sys.exit(0 if passed else 1)
PY
```

```text
CLI exit: 0
Expected outstanding IDs: ['B', 'C']; actual IDs: ['A']
Expected outstanding total: 75; actual total: 100
SHA256 report.py: 642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77
SHA256 test_report.py: 49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645
Original-outcome CLI check: FAIL
```

Exit status: **1**, the expected failure of this assessment check. It did not modify the implementation or provided tests.

**Coverage limits.** There is no persistent service, external integration, project CI configuration, or other runner in the supplied two-file fixture. No server or temporary project data was created, so no cleanup was needed. The fixture has one paid and two fully unpaid invoices; partial payments, credit notes, currencies, rounding, unavailable data, and actual debtor identities are not represented. Here `unpaid` is sufficient to establish outstanding B/C and 25 + 50 = 75. No broader accounting semantics or ability to contact the correct debtor is claimed. The decisive primary path already fails; green paid-contract tests do not override it.

## stale-acceptance

### Task response: safe delivery decision

**Preserve the topic and the dirty original checkout. Refresh current acceptance and integration evidence before considering a merge. Do not merge, synchronize the dirty checkout, or clean the branch from this recorded state.** No Git mutation was executed.

The record reports approval for head `aaaa1111` against `main` at `bbbb2222`, with hosted tests for `aaaa1111`. It now reports head `cccc3333` and target `main` at `dddd4444`. Both content coordinates changed. The prior exact-revision acceptance receipt is invalid for the proposed current delivery, regardless of whether the additional fix looks small.

| Record/check | Reuse and required refresh |
| --- | --- |
| Original issue, intended outcome, decisions and dependency rationale | Retain as context; reconcile any scope change made by the extra fix. They remain useful records, not current implementation approval. |
| Independent approval for `aaaa1111` / `bbbb2222` | Retain as historical review evidence. Unchanged, unaffected reasoning may be reused after comparison; it cannot approve `cccc3333` / `dddd4444`. Refresh the actual patch fingerprint and obtain independent review/acceptance for affected code and integration context. Do not manufacture PASS from an author self-check. |
| Hosted tests passed for `aaaa1111` | Historical deterministic evidence only. Run supported local CI equivalents and current required hosted checks for the proposed head and current target integration; inspect failures, conditions, and required-check policy. No current pass follows from the old run. |
| Target `bbbb2222` | Preserve in history. Refresh current `main` tip, merge-base, actual diff and mergeability against `dddd4444`; establish whether target changes affect behavior or checks. Any subsequent target/head movement invalidates the corresponding acceptance receipt again. |
| Stacked child still targeting this topic | Active dependency blocks cleanup. Inventory the stack and merge parents before children. Do not delete/retarget blindly. After authorized parent integration and the child's retarget/rebase as needed, recompute the child's patch identity and refresh its independent acceptance and required checks. Old stacked approval does not approve a rewritten child patch. |
| Original checkout's uncommitted notes | Preserve them and record branch/upstream/SHA and dirty/untracked paths. They block automatic fast-forward synchronization of that checkout. No reset, discard, forced checkout, or stash without consent. |
| Topic created by Factory | Useful ownership evidence, but only one cleanup precondition. It proves neither integration nor absence of useful or dependent work. |

**Next delivery sequence, conditional on authorization and repository policy:**

1. Read-only refresh the repository/PR identity, original checkout/starting branch/upstream/SHA and dirty paths; current head, target, merge-base, patch digest, protection rules, required checks, active worktrees and dependent PRs. The supplied short SHAs are a scenario record, not live observations. No repo URL, actual refs, CI links, or working-tree inventory was provided, so I have not pretended to execute a live guard or fetch.
2. Compare the extra fix and target changes with the accepted patch. Re-run relevant deterministic and integration checks and obtain exact-content independent Code Review/Product Validation, plus Interface Review if the change affects UI. Retain unaffected prior reasoning as supporting evidence only. Record current target/head/fingerprint, reviewer, verdict, evidence and prerequisites. If rebasing, retargeting, or another fix changes content, refresh the relevant acceptance again.
3. Once all actual policy gates and authorization are satisfied, integrate the parent in stack order using the established merge strategy and an expected-head operation. Confirm the resulting merge revision and the delivered target state. No authorization to execute that mutation is inferred from this decision task.
4. Restore/synchronize the original checkout only after the notes have been safely handled under the user's direction and the checkout is clean. Confirm the recorded starting branch; prefer fast-forward only if ancestry allows it. If dirty or divergent, report that precise unfinished step and preserve the checkout. A remote merge does not synchronize local files. Verify the integrated SHA and content locally afterward.
5. Resolve the child's base/dependency status and refresh its rewritten patch acceptance before child delivery. Immediately before any branch/worktree cleanup, refresh positive ownership, exact expected tip, protections, active use, dirty state, dependency state and integration proof. Keep the topic while the child still depends on it or any condition is unknown.

**Cleanup proof must match the merge strategy.** For a normal merge, require source-head ancestry in the intended target. For squash, require authoritative merged-PR evidence for that exact source head and intended target plus a merge commit reachable from the target. For rebase, retain the topic if no authoritative mapping proves the integrated patch; patch-id similarity alone is insufficient. Preserve a topic that advanced after merge, contains useful unmerged commits, is dirty, is in active use, has dependencies, or is original/default/protected. For any later remote deletion, re-read the live tip and use an explicit expected-SHA lease; use safe local deletion only when permitted by ancestry and refreshed state. Do not force-delete to make cleanup succeed. Use the app lifecycle for app-managed worktrees if applicable.

**Current delivery status:** current revision acceptance is **INCONCLUSIVE / not established**, and old approval is stale; merge is not ready. Synchronization is blocked by the reported uncommitted notes. Cleanup is blocked by the reported stacked child and absent current integration/safety proof. No deployment or environment evidence was supplied; no delivery, synchronization, or cleanup is claimed complete.

### Evidence and limits

Applied GitHub Workflow and Release with their linked `references/delivery.md`. The case's recorded PR state is the only repository-state evidence for this case. It is sufficient to choose preservation and refresh as the next action; it is insufficient to certify live refs, protection policy, integration, release, or deletion safety. No Git command, hosted check, merge, fetch, stash, synchronization, retarget, branch/worktree deletion, or external record write was performed.

## Read-only inspection record

The initial inventory command was:

```sh
pwd && rg --files /Users/Craig/Developer/Projects/factory/plugins/factory/skills && cat /Users/Craig/Developer/Projects/factory/evaluations/cases.json
```

Result: working directory `/Users/Craig/Documents/Codex/2026-10-29/ca`; 17 candidate skill definition paths; the three cases reproduced by the sections above. `cases.json` SHA-256 was `c619980afb81bb6d220aebe2e7f5c80212770bc842a66cce7e05355f7189f9eb`.

The selected candidate skill definitions and linked verification, code-quality and delivery references were read with `Path.read_text()` in Python stdin scripts (`PYTHONDONTWRITEBYTECODE=1`). Interface Review was additionally read with `cat` for the CLI behavior assessment. No entire-repository tour or unrelated source read was performed. The source manifest below records inspected content, not a Git commit assertion:

| Path relative to `plugins/factory` | SHA-256 |
| --- | --- |
| `skills/factory/SKILL.md` | `28ca0c75b0ca722a13d8fc73184a8cd8a873fbe87b9847120ee87f28ac002dce` |
| `skills/product-discovery/SKILL.md` | `4fe5913b87115e8c79fb21e48caf6a12486a1b2fd26b810b448d7bdf2c6d85e3` |
| `skills/requirements/SKILL.md` | `670f042de179ed581e2622e4e8c5b1e9cf1714c375cc4dd330057dcdfa727ed2` |
| `skills/codebase-research/SKILL.md` | `a745dcf972a3cb6cd6c8cec2828c8c9320f66a5dcbdcd4959df986f08ca22e6d` |
| `skills/architecture/SKILL.md` | `3e985764c032518670493679a1cf179cdb82b7d36805724bc2383f6a98199eff` |
| `skills/testing/SKILL.md` | `5c5411f3f92ad65f4f7db11c913c47a50512e25c49d06fd5ff5f019c35b1b369` |
| `skills/code-review/SKILL.md` | `928ceb25d6758ddd76f166c53cf6d9d49c84f61b8765d56a7c2d69430f19bd91` |
| `skills/product-validation/SKILL.md` | `dc88b581b15c6349178a01ceba5e11a575b1cb8bfcb3929d0ca16864708d8538` |
| `skills/interface-review/SKILL.md` | `e134012615c8717f2a08b64d6b627be2a66edd88bbd562656258f49d9340233d` |
| `skills/github-workflow/SKILL.md` | `5ae78cc688de29ffeebac51336877323f2cf62b420583d09305f4135fa796830` |
| `skills/release/SKILL.md` | `65e8749fc4a71a2ff5144bfd603c41e1d273cc3a419e911f8e11f9f883a7a5ec` |
| `references/verification.md` | `887484e49c22e8ed34701c1700c7967cc64941a5bdee7e610e248ab12cfc7d92` |
| `references/code-quality.md` | `d62f71541e8977b2ff4bc49f64bbd1e2f8aaaa5dc21abbc20246ab463a4a0f01` |
| `references/delivery.md` | `074597563ffe4c97a05e21d4e02a87e4b670647ae6fa508837e6fef486f1595b` |

Hashes were calculated by a read-only Python stdin loop over those exact paths with `hashlib.sha256(p.read_bytes()).hexdigest()`. All inspection/read commands exited 0. The only nonzero task execution was the deliberately failing original-outcome CLI check documented above. No evaluation scores were assigned.


## wrong-product-outcome — rerun after verification-reference reread

The evaluator was notified that `references/verification.md` changed during the initial run. I reread the current reference and both invoice fixture files, then repeated the submitted test, actual CLI, and original-outcome assertion through captured subprocess executions. The original source manifest above remains the historical initial inspection; it has not been relabeled as the current reference.

- Initial inspected `references/verification.md` SHA-256: `887484e49c22e8ed34701c1700c7967cc64941a5bdee7e610e248ab12cfc7d92`.
- Reread/current inspected `references/verification.md` SHA-256: `779795f93ced1cbea0e181b717ef6e71c6bfc904d5076cd081a10a76e6b80650`.
- The reread includes the durable Windows cleanup limitation: Windows uses `taskkill`, and descendants cannot be proven stopped if their process leader has already exited; that launch condition is INCONCLUSIVE. Windows CI does not substitute for the POSIX-specific descendant tests. Actual runner reports and platform coverage must be inspected for a flow using them.

**Rerun decision:** deterministic PASS for the single paid-report contract; Code Review FAIL against original intent; inspected CLI behavior FAIL; original product outcome FAIL. `report.py:12–13` still selects paid A and totals 100. The original request requires the supplied unpaid B/C and total 75. The original-outcome assertion failed with return code 1 after consuming a successful real CLI process. Return the contract mismatch to Requirements and Build; do not approve or repair this snapshot. No code or test change was made.

This reread does not change the product verdict. These executions ran on `darwin` as short-lived, synchronous subprocesses; the invoice CLI starts no persistent service and creates no temporary project data. No launched descendant-process cleanup contract or Windows behavior was exercised. The new Windows cleanup caveat therefore does not invalidate the observed local invoice output, but no Windows process-tree cleanup or cross-platform descendant-test PASS is claimed. No helper verification-runner PASS, hosted-CI equivalence, unseen diff, or later commit acceptance is claimed. Missing hosted/platform evidence remains INCONCLUSIVE for that scope.

The two fixture hashes before and after every command match the original snapshot. Machine-readable evidence is saved at `/Users/Craig/Developer/Projects/factory/evaluations/results/candidate-execution.json`. Each entry includes the actual argument array, working directory, return code, stdout, stderr, environment override and fixture hashes. The full captured execution evidence follows; the `-c` argument contains the complete assertion program, including its nested actual CLI invocation.

```json
{
  "schema_version": 1,
  "case_id": "wrong-product-outcome",
  "captured_at_utc": "2026-10-29T18:37:56.927082+00:00",
  "platform": "darwin",
  "python_executable": "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3",
  "fixture_root": "/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices",
  "verification_reference": {
    "path": "/Users/Craig/Developer/Projects/factory/plugins/factory/references/verification.md",
    "initial_inspected_sha256": "887484e49c22e8ed34701c1700c7967cc64941a5bdee7e610e248ab12cfc7d92",
    "reread_inspected_sha256": "779795f93ced1cbea0e181b717ef6e71c6bfc904d5076cd081a10a76e6b80650",
    "note": "Reference reread after its Windows cleanup limitation was added; initial digest preserved as historical inspection identity."
  },
  "fixture_sha256_before": {
    "report.py": "642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77",
    "test_report.py": "49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645"
  },
  "fixture_sha256_after": {
    "report.py": "642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77",
    "test_report.py": "49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645"
  },
  "fixture_unchanged": true,
  "commands": [
    {
      "name": "provided_tests",
      "argv": [
        "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3",
        "-m",
        "unittest",
        "-v"
      ],
      "cwd": "/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices",
      "returncode": 0,
      "stdout": "",
      "stderr": "test_paid_report_contract (test_report.ReportTests.test_paid_report_contract) ... ok\n\n----------------------------------------------------------------------\nRan 1 test in 0.000s\n\nOK\n",
      "fixture_sha256": {
        "report.py": "642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77",
        "test_report.py": "49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645"
      },
      "environment_override": {
        "PYTHONDONTWRITEBYTECODE": "1"
      },
      "timeout_seconds": 30
    },
    {
      "name": "actual_cli",
      "argv": [
        "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3",
        "report.py"
      ],
      "cwd": "/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices",
      "returncode": 0,
      "stdout": "{\"invoices\": [{\"id\": \"A\", \"status\": \"paid\", \"amount\": 100}], \"total\": 100}\n",
      "stderr": "",
      "fixture_sha256": {
        "report.py": "642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77",
        "test_report.py": "49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645"
      },
      "environment_override": {
        "PYTHONDONTWRITEBYTECODE": "1"
      },
      "timeout_seconds": 30
    },
    {
      "name": "original_outcome_assertion",
      "argv": [
        "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3",
        "-c",
        "import json\nimport subprocess\nimport sys\ncli_argv = [sys.executable, \"report.py\"]\nproc = subprocess.run(cli_argv, capture_output=True, text=True, check=False, timeout=15)\nprint(\"CLI argv: \" + json.dumps(cli_argv))\nprint(\"CLI returncode: \" + str(proc.returncode))\nprint(\"CLI stdout: \" + proc.stdout.rstrip())\nprint(\"CLI stderr: \" + proc.stderr.rstrip())\nassert proc.returncode == 0, \"CLI must exit successfully before evaluating its product result\"\nactual = json.loads(proc.stdout)\nactual_ids = [row[\"id\"] for row in actual[\"invoices\"]]\nexpected_ids = [\"B\", \"C\"]\nexpected_total = 75\nprint(\"Expected outstanding IDs: \" + repr(expected_ids) + \"; actual IDs: \" + repr(actual_ids))\nprint(\"Expected outstanding total: \" + str(expected_total) + \"; actual total: \" + str(actual[\"total\"]))\nassert actual_ids == expected_ids and actual[\"total\"] == expected_total, \"Original outstanding-invoice outcome failed: expected B/C and 75; observed \" + repr(actual_ids) + \" and \" + str(actual[\"total\"])\n"
      ],
      "cwd": "/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices",
      "returncode": 1,
      "stdout": "CLI argv: [\"/Library/Frameworks/Python.framework/Versions/3.14/bin/python3\", \"report.py\"]\nCLI returncode: 0\nCLI stdout: {\"invoices\": [{\"id\": \"A\", \"status\": \"paid\", \"amount\": 100}], \"total\": 100}\nCLI stderr: \nExpected outstanding IDs: ['B', 'C']; actual IDs: ['A']\nExpected outstanding total: 75; actual total: 100\n",
      "stderr": "Traceback (most recent call last):\n  File \"<string>\", line 17, in <module>\n    assert actual_ids == expected_ids and actual[\"total\"] == expected_total, \"Original outstanding-invoice outcome failed: expected B/C and 75; observed \" + repr(actual_ids) + \" and \" + str(actual[\"total\"])\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: Original outstanding-invoice outcome failed: expected B/C and 75; observed ['A'] and 100\n",
      "fixture_sha256": {
        "report.py": "642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77",
        "test_report.py": "49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645"
      },
      "environment_override": {
        "PYTHONDONTWRITEBYTECODE": "1"
      },
      "timeout_seconds": 30
    }
  ],
  "conclusions": {
    "provided_deterministic_contract": "PASS",
    "code_review_against_original_request": "FAIL",
    "cli_interface_behavior_against_original_request": "FAIL",
    "original_product_outcome": "FAIL"
  }
}
```
