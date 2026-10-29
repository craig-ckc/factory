# Independent behavioral comparison

Evaluator: `independent-behavior-grader:/root/behavior_grading (2026-10-29)`. Assessment date: 2026-10-29.

Both versions PASS all three seeded cases. Every baseline PASS remains PASS. The candidate adds detail, but this paired result demonstrates no case-level behavioral improvement or regression. Judgments use the observable decisions and execution evidence, not headings or phrase matches.

| Case | Baseline | Candidate | Evidence supporting both judgments |
| --- | --- | --- | --- |
| unclear-feature | PASS | PASS | Four operations coordinators and reduced handover preparation effort remain central. Supplied stakeholder context is separated from unmeasured costs/benefits. Both challenge stale summaries and define a representative timing, verification and accuracy comparison. Proposed scope remains conditional, with rationale recorded and consequential choices pending. Neither invents research or claims implementation readiness gaps have been resolved. |
| wrong-product-outcome | PASS | PASS | Both execute and retain evidence for the supplied test and actual CLI, distinguish the narrow deterministic PASS from the original product FAIL, identify paid A/100 versus outstanding B/C totaling 75, withhold approval, return the mismatch to Requirements and make no repair. Detecting this product failure is the required successful evaluation behavior. |
| stale-acceptance | PASS | PASS | Both require acceptance/check refresh for changed head and target, retain prior evidence as history, protect the dirty original notes and stacked child, preserve the topic and execute no Git mutation. The scenario supports a safe next-action decision, not live merge acceptance. |

The unclear-feature briefs correctly leave missing evidence and consequential scope/service choices unresolved. That is not an evaluation failure. Likewise, candidate's current delivery acceptance being INCONCLUSIVE is a correct conclusion about the recorded PR state, not an inconclusive behavioral grade.

## Execution evidence and limits

I inspected the retained task outputs and unsigned performer-generated subprocess records. Each record contains argv, cwd, exit status, stdout/stderr and matching before/after fixture hashes. These support the performers' reruns; they are not signed transcripts or independent proof of all historical first-run tool calls. I did not directly observe those earlier calls.

I independently ran the supplied unittest and actual CLI with bytecode writes disabled. The one supplied test passed (exit 0), and the CLI returned paid A and total 100 (exit 0). A direct original-outcome probe through the CLI failed (exit 1); a further independent comparison after the performer reruns confirmed the same mismatch. The source hashes stayed unchanged. Reproduction from `evaluations/fixtures/invoices` is `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_report.py` and `PYTHONDONTWRITEBYTECODE=1 python3 report.py`; compare its JSON with outstanding IDs B/C and total 75. No repair was made.

| Retained evidence | SHA-256 |
| --- | --- |
| `baseline.md` | `456dc88841537bf4bb492ddcfc8b9e91f6e49b736d18cc100ecb9b48eb4a4fc8` |
| `candidate.md` | `a3a1b6632c7ce1965a57641f482bffe4d3e7c0fc1016ada5401890bdc4cfaf4e` |
| `baseline-execution.json` | `9aba50d10800f3dc5b72dcd78f9dcd50aae9b8f5ba0d1ffcb4c9132ec6fb099e` |
| `candidate-execution.json` | `656766cdb89000fd13a48fd39a2692cdcb86d05a8e99d93a65bb1b91242f6337` |
| `fixtures/invoices/report.py` | `642bd95cd04cff52ebfbf4bdde07c0f9dd10ca118283b950681899f99efe8d77` |
| `fixtures/invoices/test_report.py` | `49647379259cd28e42a2dcaa316341953b88039b11d48b83d802cff29430d645` |

The dataset receipt is the SHA-256 of `cases.json` bytes: `c619980afb81bb6d220aebe2e7f5c80212770bc842a66cce7e05355f7189f9eb`. Both outputs use those requests and the same two-file fixture. The supplied stakeholder note is the only handover domain evidence; the invoice is seeded data, and the PR state is a recorded scenario. No observed customer research, live Git state or broader invoice semantics are inferred.

The baseline artifact was subsequently normalized by removing exactly two trailing spaces from each of header lines 3 and 4. Restoring those four bytes reproduces its previously assessed SHA-256 `e1b2ed5cf188b107b38e37a70c7ece00933461d61407d8ffaae0654cf17cff0a`; no other bytes changed. Its receipt now binds the normalized artifact hash above, and all verdicts remain unchanged.

## Revision binding

Baseline revision: `647d6b0885caf7c3e47f907a7898daf07ac2090f`. The extracted baseline is not a Git checkout. I independently compared its ten applicable SKILL.md files plus linked `references/code-quality.md` byte-for-byte with the files at that Git commit; all eleven matched.

Candidate revision: `content-sha256:ce72cdc716c6491276e06e5c291df81892de83b197e32678be3a24c4b7d5e537`. This is a source-content identity, not an assertion about a future commit. It covers all 17 SKILL.md files and all 10 files under `plugins/factory/references/` in the manifest below. Compute SHA-256 of each file's bytes, sort by its relative POSIX path, encode each line as `<sha256><two spaces><relative path><newline>` in UTF-8, then SHA-256 that concatenation. The manifest identifies the snapshot; unexercised files do not gain behavioral coverage from inclusion.

I cross-checked all fourteen paths the candidate reported reading. Thirteen original hashes match the final files. `references/verification.md` initially differed: the task output recorded `887484e49c22e8ed34701c1700c7967cc64941a5bdee7e610e248ab12cfc7d92`, while the final file is `779795f93ced1cbea0e181b717ef6e71c6bfc904d5076cd081a10a76e6b80650`. The candidate preserved that history, explicitly reread the current reference and reran the invoice assessment. The appended output and execution record contain the current hash. The noted change concerns a Windows process-cleanup limitation; this local fixture launches no persistent service. No Windows or descendant-cleanup result is claimed. Thus the receipt binds the final inspected content without silently treating the first read as current.

| Path relative to `plugins/factory` | SHA-256 |
| --- | --- |
| `references/code-quality.md` | `d62f71541e8977b2ff4bc49f64bbd1e2f8aaaa5dc21abbc20246ab463a4a0f01` |
| `references/delivery.md` | `074597563ffe4c97a05e21d4e02a87e4b670647ae6fa508837e6fef486f1595b` |
| `references/design/accessibility.md` | `8c5ec4026dd1ba048cd3f50351153e1b5d2f2c03a5745b85690e7a976e74261b` |
| `references/design/color.md` | `f7c96a5ff83a82c0cb991aa2a165f787238a5ed400e5288d9e594ce7768086be` |
| `references/design/interface-writing.md` | `a1a259c46057aeaaaa681e904d6868e137afd6fc7bef09f9ede911270eb67d76` |
| `references/design/layout.md` | `ec4e15bc5d178fadd0f2d7f58c61d2056c59d6024a163b99af815b8275326e92` |
| `references/design/motion.md` | `41507c9530343c4fc5a434cc6906a6b2838fcea364bace79c90019e466fee884` |
| `references/design/typography.md` | `f67cabba4d8925f64d3b8e4fb487357337d5395df5d79ae1f4d41b51ead0a4b0` |
| `references/learning.md` | `54d6fbbe2273f29d1e267a55b3a61da34115add06b716958fdefff31a50f493c` |
| `references/verification.md` | `779795f93ced1cbea0e181b717ef6e71c6bfc904d5076cd081a10a76e6b80650` |
| `skills/architecture/SKILL.md` | `3e985764c032518670493679a1cf179cdb82b7d36805724bc2383f6a98199eff` |
| `skills/code-review/SKILL.md` | `928ceb25d6758ddd76f166c53cf6d9d49c84f61b8765d56a7c2d69430f19bd91` |
| `skills/codebase-research/SKILL.md` | `a745dcf972a3cb6cd6c8cec2828c8c9320f66a5dcbdcd4959df986f08ca22e6d` |
| `skills/factory/SKILL.md` | `28ca0c75b0ca722a13d8fc73184a8cd8a873fbe87b9847120ee87f28ac002dce` |
| `skills/github-workflow/SKILL.md` | `5ae78cc688de29ffeebac51336877323f2cf62b420583d09305f4135fa796830` |
| `skills/implementation/SKILL.md` | `c469156a6d18f428ca0d5aa73c66e2efd072c29b190756c21e2640aa0034c9f1` |
| `skills/interface-build/SKILL.md` | `a5ab9253fc3b6aa7053d7a22dec7bcadd31326bb1ea31a5058eebb3179d9d9c4` |
| `skills/interface-design/SKILL.md` | `6d1b96c7afa4b6de7bb3b534bb3ad7d58935e5660154a30c6d681e019cfbc77f` |
| `skills/interface-review/SKILL.md` | `e134012615c8717f2a08b64d6b627be2a66edd88bbd562656258f49d9340233d` |
| `skills/product-discovery/SKILL.md` | `4fe5913b87115e8c79fb21e48caf6a12486a1b2fd26b810b448d7bdf2c6d85e3` |
| `skills/product-validation/SKILL.md` | `dc88b581b15c6349178a01ceba5e11a575b1cb8bfcb3929d0ca16864708d8538` |
| `skills/prototype/SKILL.md` | `be04bdf34820f68ce179e567b24052a1bf6cf6dda6b0279572e8c89c91b2ad0c` |
| `skills/refactoring/SKILL.md` | `d341043870c59c99003770f87d45c4f89fca2a45c7c0aee38b5a31c9d79b48aa` |
| `skills/release/SKILL.md` | `65e8749fc4a71a2ff5144bfd603c41e1d273cc3a419e911f8e11f9f883a7a5ec` |
| `skills/requirements/SKILL.md` | `670f042de179ed581e2622e4e8c5b1e9cf1714c375cc4dd330057dcdfa727ed2` |
| `skills/testing/SKILL.md` | `5c5411f3f92ad65f4f7db11c913c47a50512e25c49d06fd5ff5f019c35b1b369` |
| `skills/ui-inspection/SKILL.md` | `2a3fbacd5e5fcdfef2b6b6cf1908fa7dc97ec083b2998ab755cc729073911fee` |

## Scope of the result

No material rubric mismatch remains in the inspected case responses. Retained execution provenance remains limited as described above. These three cases establish only these behaviors on this prompt/fixture set; they do not establish universal reliability, production readiness, provider adoption, helper-runner correctness or cross-platform execution. Packaging/helper tests are separate evidence and were not used to manufacture a behavioral PASS.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/compare_evaluations.py evaluations/results/baseline.json evaluations/results/candidate.json` exited 0 and returned overall PASS, with PASS/PASS for each case. The helper validates receipt shape, maintained case membership and artifact/dataset hashes; it does not independently judge these responses.
