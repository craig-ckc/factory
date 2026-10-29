# Baseline task responses

Date: 2026-10-29
Baseline skill snapshot: /Users/Craig/Documents/Codex/2026-10-29/ca/work/factory-run/baseline/plugins/factory/skills
Designated baseline revision: 647d6b0885caf7c3e47f907a7898daf07ac2090f

I performed the requests using the baseline Factory skill definitions. I did not inspect a rubric, candidate skill definitions, another evaluator's output, or comparison receipts. This report contains task judgments, not evaluation scores. No Git or external mutations were performed. The invoice fixture was not changed.

## unclear-feature

### Task response

**Actor and outcome.** Four operations coordinators prepare the weekly Friday handover email. The intended outcome is to reduce the time and effort of producing an accurate handover that communicates current status and blockers. “Add AI summaries” is the requested solution; it is not yet established as the cause of, or remedy for, the delay.

**Available evidence.** The stakeholder note says coordinators copy status and blockers from existing reports into an email. Those reports contain manually maintained summaries that are sometimes stale. The assertion that handover takes too long has no measured baseline. No interviews, analytics, sample reports, source-system implementation, budget, or permission for external AI processing were supplied.

**Hypotheses, not findings.** Copying between reports and email may be the principal cost. Summary freshness, source selection, checking facts, or reconciling contradictory information may instead account for much of the delay. AI could shorten drafting but increase verification work. A generated summary could reproduce stale information; the note does not establish whether the underlying status and blocker fields are current.

The smallest decisive assumption is that generating a new summary reduces total preparation time, including checking and corrections, without reducing handover accuracy. A second dependency is whether current status and blocker information can be reliably obtained from the reports.

**Proposed scope for a first slice, subject to the decision below.**

- Produce a reviewable draft from the selected reports' status and blocker information. Preserve a reference to each source so a coordinator can verify it.
- Treat freshness as explicit evidence: use available source metadata if it exists; otherwise show that freshness is unknown. Do not present a stale or unverified manually maintained summary as confirmed current information.
- Require coordinator review before using the draft. Preparing a draft and sending the email are separate actions; automated sending is outside this brief.
- Keep source data within currently authorized processing boundaries. Do not choose or integrate an external AI provider without permission, suitable data-handling constraints, and budget.
- Keep AI optional while testing whether source reuse and a simpler assembly workflow meet the outcome. Do not add a parallel summarization system solely because the feature request names AI.

This is a behavior-level brief, not a claim that an AI implementation is ready to build. It is premature to choose the provider, data flow, UI, source adapter, or deployment design without inspecting the actual handover/report system. The requested implementation-ready state still needs the decisions and evidence below.

**Acceptance evidence.** Before Build, agree a representative set of report snapshots and a coordinator task, record current end-to-end preparation time and correction effort, and agree the required improvement. No numerical saving is asserted or silently invented.

For the proposed draft slice, acceptance should demonstrate that:

1. The selected reports' relevant statuses and blockers appear in the draft, and each factual statement can be checked against its source.
2. Stale or unestablished freshness is visible to the reviewer; conflicting, absent, or unreadable information does not become an invented claim.
3. A coordinator can inspect and correct the draft before using it.
4. A representative comparison measures total preparation plus verification/correction time, and checks accuracy against the source records. The agreed time improvement must be achieved without introducing material factual errors.
5. No report content is transmitted outside the approved boundary.

These are proposed acceptance conditions. The report examples, timing baseline, improvement threshold, supported sources, and review decision have not yet been supplied or validated. Therefore product success is unproven.

**Codebase and architecture handoff.** No handover repository or architecture was provided or inspected. Before coding, trace report storage → current summary/status/blocker representation → current handover preparation → email draft/export, along with source consumers, tests, freshness/version metadata, access control, and existing integration patterns. Establish where that flow already belongs and reuse it. Only after that inspection should the builder define concrete modules, interfaces, failure handling, and data contracts. There is no evidence here supporting a new AI service boundary or a lasting architectural abstraction.

**Issue-style change record.**

- Original request: “Add AI summaries to the weekly handover because handover takes too long.”
- Original intent retained: reduce coordinator effort while preserving an accurate, current handover.
- New evidence considered: the workflow copies existing report information; summaries already exist and can be stale; no timing or external-processing authorization exists.
- Proposed direction change: first validate the preparation bottleneck and source freshness, and consider a source-based draft before committing to AI.
- Rationale: AI generation may fail to remove the actual bottleneck and may repeat stale information.
- Status: recommendation awaiting a scope decision; no replacement implementation or product-intent change has been represented as approved.
- Next decision: approve this bounded source/draft approach and its evidence plan, or retain AI as a required solution and first resolve data-processing permission, budget, source access, and accuracy expectations. Preserve the same coordinator outcome either way.

An author self-check found the missing source contract, unmeasured outcome, and unapproved external processing to be material readiness gaps. Independent specification review has not occurred. Obtain it before Build when available and permitted.

### Commands and evidence

Read the case text from:
~~~sh
cat /Users/Craig/Developer/Projects/factory/evaluations/cases.json
~~~
Result: the stakeholder note and constraints reproduced above; no handover product source was supplied.

Read the baseline skill files using:
~~~sh
cat <baseline-skill-root>/factory/SKILL.md
cat <baseline-skill-root>/product-discovery/SKILL.md
cat <baseline-skill-root>/requirements/SKILL.md
cat <baseline-skill-root>/codebase-research/SKILL.md
cat <baseline-skill-root>/architecture/SKILL.md
~~~
Result: used outcome-first discovery, fact/hypothesis separation, observable acceptance, issue/spec decision history, and evidence-grounded architecture. No implementation, experiment, interview, external service, or contact was performed.

## wrong-product-outcome

### Task response

**Deterministic conclusion: PASS for the supplied paid-report contract and one supplied test.** The actual CLI emits paid invoice A with total 100. The provided unittest expects A and 100 and passes. This establishes the submitted contract on the supplied fixed data; it does not establish the original user outcome.

**Product conclusion: FAIL for the inspected content.** The original request is to show outstanding invoices and their outstanding total so the user knows who to chase. The supplied data contains unpaid invoices B (25) and C (50), so the observable expected result is B and C with total 75. The actual CLI omits both and returns the paid invoice instead. The original-outcome assertion against the real CLI fails.

**Code review finding — P1: the report selects the wrong invoice population.** In report.py:12–13, report() filters status == 'paid' and sums that subset. A user seeking overdue/outstanding work receives a paid invoice and a total of 100 rather than the unpaid invoices and total of 75. Reproduce with the CLI and the original-outcome assertion below. The test at test_report.py:7–10 encodes the same contradictory paid-report contract, which explains the green deterministic result. Approval for the original request is withheld.

Return the contract mismatch to Requirements and reconcile it with the original user intent before Build. Then revise the implementation and regression coverage under that corrected contract and repeat independent product validation. I did not repair the fixture.

**Inspected content and scope.**

- Fixture root: /Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices
- report.py SHA-256: 642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77
- test_report.py SHA-256: 49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645
- The enclosing repository HEAD was 647d6b0885caf7c3e47f907a7898daf07ac2090f, but the fixture directory was untracked. The hashes above identify the content actually assessed; I do not attribute these untracked fixture files to that commit.
- No tracked submitted patch or before/after diff was available. This was an independent assessment of the supplied implementation, test, and executed CLI, not approval of an unseen PR diff.
- The supplied fixture uses a fixed invoice list and exposes no CLI arguments, customer contact data, network integration, or permission model. I did not claim broader status/partial-payment semantics, customer identification, production behavior, or error/permission coverage. The primary user outcome already fails on the supplied mixed paid/unpaid data.
- Hashes were identical before and after execution. No fixture files were edited, and PYTHONDONTWRITEBYTECODE=1 prevented local import bytecode writes.

### Commands and results

Inspected the only supplied fixture files:
~~~sh
rg --files -g '!__pycache__/**' /Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices
nl -ba report.py
nl -ba test_report.py
shasum -a 256 report.py test_report.py
~~~
Result: report.py has three invoices: A paid/100, B unpaid/25, C unpaid/50. Its report() selects paid invoices and sums their amounts. The single supplied test expects A and 100. Hashes are recorded above.

Read repository instruction locations from /AGENTS.md through the fixture's AGENTS.md. None existed in the searched ancestor locations.

All execution below used working directory:
~~~text
/Users/Craig/Developer/Projects/factory/evaluations/fixtures/invoices
~~~

Actual CLI:
~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 report.py
~~~
Exit 0:
~~~json
{"invoices": [{"id": "A", "status": "paid", "amount": 100}], "total": 100}
~~~

Provided deterministic test:
~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_report.py
~~~
Exit 0:
~~~text
test_paid_report_contract (test_report.ReportTests.test_paid_report_contract) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
~~~

Original-outcome check using the actual CLI, with no test file written:
~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json
import subprocess
import sys
observed = json.loads(subprocess.check_output([sys.executable, 'report.py'], text=True))
expected = {'invoices': [{'id': 'B', 'status': 'unpaid', 'amount': 25}, {'id': 'C', 'status': 'unpaid', 'amount': 50}], 'total': 75}
print('Observed CLI:', json.dumps(observed, sort_keys=True))
print('Original-outcome expectation for supplied fixture:', json.dumps(expected, sort_keys=True))
assert observed == expected, 'CLI does not show outstanding invoices B and C with outstanding total 75'
PY
~~~
Exit 1:
~~~text
Observed CLI: {"invoices": [{"amount": 100, "id": "A", "status": "paid"}], "total": 100}
Original-outcome expectation for supplied fixture: {"invoices": [{"amount": 25, "id": "B", "status": "unpaid"}, {"amount": 50, "id": "C", "status": "unpaid"}], "total": 75}
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
AssertionError: CLI does not show outstanding invoices B and C with outstanding total 75
~~~

Revision/content audit:
~~~sh
git rev-parse --show-toplevel HEAD
git status --short -- .
git diff -- .
git ls-files --stage -- .
~~~
Results:
~~~text
/Users/Craig/Developer/Projects/factory
647d6b0885caf7c3e47f907a7898daf07ac2090f
?? ./
~~~
The diff and tracked-file listing emitted nothing because these fixtures are untracked.

A first status/diff attempt used evaluations/fixtures/invoices relative to the already nested fixture directory and produced:
~~~text
warning: could not open directory 'evaluations/fixtures/invoices/evaluations/fixtures/': No such file or directory
~~~
That attempt established no fixture cleanliness. It was corrected to the commands with -- . above.

After execution:
~~~sh
shasum -a 256 report.py test_report.py
git status --short -- .
~~~
Result: the same two hashes and the same untracked-directory status.

Read baseline Testing, Code Review, and Product Validation skills, plus the baseline code-quality reference linked by Code Review:
~~~sh
cat <baseline-skill-root>/testing/SKILL.md
cat <baseline-skill-root>/code-review/SKILL.md
cat <baseline-skill-root>/product-validation/SKILL.md
cat <baseline-plugin-root>/references/code-quality.md
~~~
Result: deterministic verification and actual outcome acceptance were assessed separately; no implementation repair was performed.

## stale-acceptance

### Task response

**Safe next action: preserve the current state and refresh acceptance for the current head and target. Do not merge, synchronize the dirty original checkout, or delete the topic yet.** The recorded approval and hosted test success are for an older result. Factory creation alone does not make this topic safe to clean up.

| Record or check | What remains reusable | What must be refreshed |
| --- | --- | --- |
| Issue/specification and rationale | The original intent, accepted scope, decision history, and links remain useful unless the new fix changes them. | Inspect the fix and target changes for scope/behavior consequences and update substantive decisions if needed. |
| Independent approval | Historical evidence for head aaaa1111 against target main at bbbb2222. It can guide the next review. | Review the changes from aaaa1111 to cccc3333 and the effect of main advancing from bbbb2222 to dddd4444. Obtain acceptance applicable to the current result. Do not carry the old approval forward as current approval. |
| Hosted tests | A historical successful run for aaaa1111. Its logs and failures/coverage context remain useful. | Run required checks for cccc3333 and its integration with current target dddd4444 under repository policy. Re-check if integration changes the tested result. |
| Delivery policy | Existing documented merge/deployment procedure can be consulted. | Read current protection rules, required checks, approvals, merge strategy, dependency state, and deployment requirements; none are supplied here. |
| Child PR | The dependency link remains a record that the child targets this topic. | Inspect the stack and plan parent-before-child integration. Retarget/update the child according to repository policy when the parent integrates, then verify its new target/diff and checks. Keep the topic while it is still needed. |
| Starting workspace record | Preserve any known original branch/upstream information and the uncommitted notes. | Record actual branch, upstream, status, and note locations before integration. The PR target main does not establish that the original checkout began on main. |

Before merge, compare both head and base changes, resolve any integration conflicts deliberately, run relevant local CI-equivalent checks where supported, and obtain current required hosted checks and independent Code Review/Product Validation for the actual result. If the change affects visuals or UI behavior, refresh Interface Review for the affected result as well. Passing tests on aaaa1111 cannot prove either the additional fix or compatibility with dddd4444. If updating the branch produces another revision, attach final evidence to that resulting revision rather than treating cccc3333 as permanently current.

The stacked child requires a safe dependency plan. Integrate this parent before the child according to repository policy, preserve the child changes, and avoid deleting a target the child still uses. A child PR still targeting the topic is a concrete reason to retain the topic now.

After an accepted merge, observe the repository's actual release/deployment path and verify the intended revision reached the intended environment where relevant. Then synchronize the original checkout back to its recorded starting branch, preferring a fast-forward while preserving the uncommitted notes. Do not reset, overwrite, drop, or silently stash them. If synchronization would conflict with those notes or history has diverged, preserve the work and report the exact blocked step.

Branch/worktree cleanup comes last. Confirm the topic is safely merged/integrated, has no useful unmerged commits, is not dirty or actively used, and has no remaining dependent PR/worktree need. Preserve the starting and protected/default branches. Use the managed-worktree lifecycle if the app owns the checkout. Retain the merged PR's discussion, review, diff, and delivery evidence even if the source branch is eventually removed.

**Evidence limitation.** This conclusion uses only the recorded state in the request: aaaa1111/bbbb2222 approved, tests passed for aaaa1111, current cccc3333/dddd4444, child targeting the topic, dirty original checkout, Factory-created topic. No repository/PR URL or live delivery context was supplied for this case. I have not inspected those revisions, current protections, the additional fix, the child patch, deployment status, or the notes. I do not assert that the new fix is safe, that the old approval is sufficient, that a merge is authorized by branch policy, or that synchronization/cleanup has completed.

### Commands and evidence

Read baseline delivery skills:
~~~sh
cat <baseline-skill-root>/github-workflow/SKILL.md
cat <baseline-skill-root>/release/SKILL.md
~~~
Result: approval and verification must cover the actual released result; preserve original workspace changes and dependent work; clean only safely integrated Factory-created topics.

No Git mutation, merge, fetch, synchronization, branch deletion, remote PR update, or deployment command was executed for this recorded-state case.

## Shared source audit

The initial inventory listed the baseline skill files and read cases.json. The applicable skill files and linked code-quality reference listed above were the only Factory instruction content used.

A read-only attempt to identify the baseline snapshot as a Git checkout:
~~~sh
git rev-parse HEAD
git status --short
~~~
with working directory /Users/Craig/Documents/Codex/2026-10-29/ca/work/factory-run/baseline exited 128:
~~~text
fatal: not a git repository (or any of the parent directories): .git
~~~
Thus the skill revision designation is the supplied baseline snapshot identity. The actual skill files were read from that path; no separate Git history for that extracted snapshot was established.

## Machine-readable invoice rerun

A rerun of wrong-product-outcome using the same baseline skills and original request retained subprocess argv, cwd, return code, stdout, stderr, and fixture SHA256 values in baseline-execution.json. The actual CLI exited 0 and returned paid invoice A with total 100. The supplied unittest exited 0 with one passing test. The original-outcome assertion against the real CLI exited 1 because outstanding invoices B and C with total 75 were absent. Deterministic verdict remains PASS for the submitted paid-report contract; product verdict remains FAIL for the original request. Both fixture hashes match the first run and remained unchanged. No fixture edits, Git mutations, or external mutations were performed. The assertion was passed through python -c in this rerun; its script and complete subprocess results are retained in the JSON evidence.
