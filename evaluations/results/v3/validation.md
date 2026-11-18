# Factory 3 validation

This is evidence for the redesign branch, not a release/adoption certificate. Baseline: `ef519c1fec50b19a836c1cbb768637f9d84d3c13` (Factory 2.2.0). The candidate plugin source is bound by [candidate-source.json](candidate-source.json); it is not identified by the old HEAD of the edited checkout.

## Results

| Check | Observed result |
| --- | --- |
| Portable project verification contract on Linux | PASS: CLI health/discovery, packaging, all 59 tests, cleanup; [transcript](checks.md) |
| Baseline/candidate workflow comparison | Both PASS on all nine identical requests; [judgment](judgment.md), [per-case reasons](judgment.json) |
| Independent source review | APPROVE after two passes; [first pass](review.md), [correction and final pass](review-round-2.md) |
| Historical 2.2.0 receipts | Still validate unchanged; they do not certify this candidate |
| Native harness adoption | Not established; see limitations below |

The reviewer found a lost assertion in the migrated broken-link regression test. The assertion was restored and its accidental duplicate removed. The reviewer confirmed that a deliberately non-rejecting checker now makes that test fail, then reran all six packaging tests. All 27 files in the [approved source map](review-round-2-content.json) were checked against their hashes after review. Pending evaluation packaging was outside that review's scope.

## Comparison scope

Separate task agents read only their assigned baseline or candidate instructions and the same requests. A third agent applied the rubric to the retained outputs. Both task agents executed the supplied invoice CLI and test; the evaluator reproduced those results. The other eight requests test decisions against supplied state. The comparison preserves every baseline success and shows no new case-level success: it supports no regression on this sample, not a causal reliability improvement.

Retained answers: [baseline](baseline.md), [candidate](candidate.md). Archived copies normalize trailing whitespace and final blank lines; command/output content is unchanged. Content-bound receipts: [baseline](baseline.json), [candidate](candidate.json). Reproduce receipt validation from the repository root:

```sh
python3 scripts/compare_evaluations.py evaluations/results/v3/baseline.json evaluations/results/v3/candidate.json --cases evaluations/recursive-cases.json
```

## Size and limits

| Active plugin surface | Baseline | Candidate |
| --- | ---: | ---: |
| Discovered skills | 17 | 6 |
| Skill-body words, including metadata | 4,500 | 2,596 |
| Markdown files under plugins/factory | 34 | 16 |
| Words in those Markdown files | 7,503 | 4,645 |

Counts use whitespace-separated words and exclude repository research, migration, and retained evaluation evidence. Fewer words are a maintenance/context reduction, not a quality score.

The review and task evaluations used available agents from this harness, not a three-provider council. No physical device, live UI, long-running recursive task, or production delivery was exercised by the decision cases. The source reviewer cross-checked supplied pinned-source snapshots, not an independent network fetch.

Codex CLI is present and exposes plugin commands, but its current marketplace list is empty; no plugin was installed into the user's environment. Claude Code and Cursor CLIs were unavailable. Native six-skill discovery/cache refresh and task behavior in each installed harness remain adoption checks. The local suite ran on Linux; hosted macOS/Windows results, if available, belong to the branch's CI checks rather than this local record.
