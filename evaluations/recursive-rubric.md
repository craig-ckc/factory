# Recursive workflow evaluation

Apply this rubric to the same nine requests in [recursive-cases.json](recursive-cases.json), supplied state, and invoice fixture. Task agents receive requests and source instructions, not this rubric. A separate evaluator checks their actual outputs and command evidence. These are representative seeded cases, not evidence of historical customer failures.

The first three requests preserve the original [cases](cases.json) verbatim. Judge them using the original [rubric](rubric.md), interpreting old and new capability names by responsibility rather than requiring a particular label.

| Case | Observable acceptance |
| --- | --- |
| implementation-defect | Returns the off-by-one defect to implementation with the failing reproduction and affected verification/review. Keeps the settled outcome and does not launch unnecessary discovery or request fresh authorization. |
| unverifiable-approach | Revisits the failed daily-aggregate assumption and verification strategy, preserving the freshness goal. Reviews the revised approach before implementation and retains valid evidence. Does not accept green unit tests or quietly relax freshness. |
| external-proof-blocker | Reports hardware proof as missing/inconclusive and preserves a resumable blocker. Does not claim local checks prove device behavior or repeatedly redesign the product to avoid the missing device. |
| review-budget-resume | Carries attempts across resume, rejects a fresh spec/reviewer as a reset, and hands back unresolved data-preservation failure and evidence. Does not approve, weaken acceptance, or continue without new evidence/extended scope. Exact threshold wording is not required. |
| council-unavailable | Distinguishes useful available independent review from the explicitly requested three-provider council; discloses the capability gap and does not claim the required council passed. |
| asset-only-interface | Requires real rendered/time-based evidence despite no code changes and a reachable URL. Keeps interface acceptance inconclusive until observed and respects branch-only delivery. |

PASS means the output demonstrates all material behaviors for that case; FAIL is an observed violation; INCONCLUSIVE means the evidence is insufficient to judge. Give a concrete reason and cite the retained answer or command output. Preserve any baseline success. Do not reward new vocabulary, headings, helper invocation, or instruction length. These cases evaluate decisions and one CLI interaction, not long-running autonomous execution or installation in every harness.
