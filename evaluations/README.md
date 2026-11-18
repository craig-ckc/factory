# Factory evaluation

Run deterministic contracts and helper behavior:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

The checks run on Linux, macOS and Windows in `.github/workflows/checks.yml`. A local run proves only its current OS. Native agent CLI discovery is an adoption check run where the provider is installed, separate from this portable suite.

For material skill changes, freeze a baseline snapshot and candidate revision, then give separate task-performing agents the same requests in [cases.json](cases.json), applicable skills and invoice fixture. Keep [rubric.md](rubric.md) with a different evaluator. Retain raw outputs in `results/`; the evaluator creates baseline/candidate JSON receipts with `revision` (immutable commit or source digest), `evaluator`, `dataset_sha256` (the cases.json bytes), and cases containing `id`, `verdict`, `reason`, relative `artifact`, and its `sha256`.

```sh
python3 scripts/compare_evaluations.py evaluations/results/baseline.json evaluations/results/candidate.json
```

The comparison verifies content receipts, the maintained case set and candidate verdicts. It does not independently judge agent output or substitute for the separate evaluator. Case requests are held constant across versions; a baseline PASS remains a PASS. The invoice fixture deliberately passes its narrow paid-report test while missing the original outstanding-report request. It is a seeded product-validation test, not production invoice software or customer research.

The existing `results/baseline*`, `results/candidate*`, and compatibility receipts describe the historical 2.2.0 work. They are not acceptance of Factory 3. Keep `cases.json` unchanged so its existing content receipts remain valid. When running those requests on Factory 3, route unclear-feature to Spec; wrong-product-outcome to Verify/Review; stale-acceptance to Deliver. The old names in the historical dataset identify responsibilities, not installed v3 entry points.

## Factory 3 recursive workflow

[recursive-cases.json](recursive-cases.json) preserves the three original request strings and adds six cases for repair routing, re-specification, external proof blockers, budget continuity, unavailable council providers, and asset-only interface acceptance. Both versions receive the same requests, fixture, tools, and side-effect limits. Task-performing agents load only their assigned source instructions; a separate evaluator uses [recursive-rubric.md](recursive-rubric.md).

Retain actual task outputs, source identities, evaluator reasons, and hashed receipts under `results/v3/`. Compare them with:

```sh
python3 scripts/compare_evaluations.py evaluations/results/v3/baseline.json evaluations/results/v3/candidate.json --cases evaluations/recursive-cases.json
```

These are bounded task evaluations using available agents, not a three-provider council or proof of native plugin installation. The [v3 validation record](results/v3/validation.md) records actual results and limits. Portable checks establish packaging/helper behavior; the task comparison establishes only the covered workflow decisions and invoice CLI interaction.

The six-task implementation record is [docs/remaining-tasks.md](../docs/remaining-tasks.md). Source differences are available in Git history; full skill bodies are maintained only in their source files.
