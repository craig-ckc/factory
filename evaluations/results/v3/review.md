# Factory redesign independent review

Verdict: **CHANGES**

Base: `ef519c1`. Reviewed the working tree, including untracked new skills, migration/research documentation, task-proof reference, and recursive evaluation cases. Reviewed-content digest: `sha256:3e646ee8e418b24d07e23107797dd755f41c470d1a5fb54301e88347511fb027` (sorted path-to-SHA256 map, compact JSON; captured in `review-content.json`). This is a read-only source review for the requested review branch, not release or merge acceptance.

## Findings

### FR-001 — Restore the broken-skill-link regression assertion

Severity: material verification regression (P2).

Location: `tests/test_packaging.py:48–51`; related duplicated assertion at lines 61–62.

The changed `test_broken_skill_reference_is_rejected` writes an invalid link into Verify but no longer calls `checker.check` or asserts rejection. Its original assertion appears to have moved to the new migration-link test, which now has two identical assertions. Consequently the named existing regression test is green even when the packaging checker never runs, weakening protection for the routing links being refactored.

Evidence: loaded the test module without editing source and ran this test with `unittest.mock.patch.object(checker, 'check', return_value=[])`. The result was `successful_with_broken_checker: True`, `checker_call_count: 0`, zero failures, zero errors. The base version called and asserted `checker.check(root)` after writing the broken skill link.

Smallest correction: restore `self.assertTrue(checker.check(root))` to the broken-skill-reference test and remove the extra duplicate from the migration-link test. Rerun the packaging tests; no new framework or test case is needed.

## Coverage and conclusions

- Traced the new Factory → Spec/Review → Build/Verify → Deliver links, bounded outer return, unavailable-proof blocker, resume counters, and independent-review limitations. No additional material routing or contradictory-condition finding was identified.
- Compared removed skills/playbooks against the six-skill design and retained references, especially rendered visual acceptance, asset and motion proof, original product intent, exact-content delivery, stacked dependencies, and safe cleanup. Marketplace identities and helper CLI source remain unchanged; the major version and retired names are explicit.
- Inspected checker/test callers, CI and project verification commands, historical evaluation requests and new recursive-case requests. Evaluation report and evaluation README work still in progress were intentionally excluded; absence of unfinished evidence is not a finding.
- Cross-checked the substantive research claims against the pinned source texts supplied in `/workspace/scratch/factory-evaluation/sources.json`: Theo's council/sol-loop, full-send/full-stop and related skills, T3 Code guidance, Matt's catalog/grilling/writing guidance, and Poteto's planning/review/principles/verification example. No inaccurate attribution identified. The document correctly labels Factory's two-return budget as its own adaptation and avoids claiming an unverified lineage.

## Limits

The lead is running candidate verification; this review does not replace those results, behavioral evaluations, or native harness discovery/adoption. No network re-fetch or independent authentication of the supplied source snapshot file was performed. README and pending evaluation report/README edits are outside this verdict. No source edits, PR comments, or subagents were made by this reviewer.
