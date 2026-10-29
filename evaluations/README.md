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

The six-task implementation record is [docs/remaining-tasks.md](../docs/remaining-tasks.md). Source differences are available in the implementation PR; full skill bodies are maintained only in their source files and Git history.
