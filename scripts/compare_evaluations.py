#!/usr/bin/env python3
"""Compare independently assessed, content-bound behavioral evaluation receipts."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def load(path, expected, dataset_sha256):
    data = json.loads(path.read_text())
    if not data.get('revision') or not data.get('evaluator'):
        raise ValueError('revision and evaluator are required')
    if data.get('dataset_sha256') != dataset_sha256:
        raise ValueError('evaluation request set changed or has no content receipt')
    cases = data.get('cases', [])
    if len(cases) != len(expected) or {case['id'] for case in cases} != expected:
        raise ValueError('case set differs from the maintained task set')
    for case in cases:
        if case['verdict'] not in ('PASS', 'FAIL', 'INCONCLUSIVE') or not case.get('reason'):
            raise ValueError('every case needs a supported verdict and reason')
        artifact = (path.parent / case['artifact']).resolve()
        if hashlib.sha256(artifact.read_bytes()).hexdigest() != case['sha256']:
            raise ValueError(f'output evidence changed: {case["id"]}')
    return {case['id']: case for case in cases}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--cases', type=Path, default=Path(__file__).resolve().parents[1] / 'evaluations/cases.json')
    args = parser.parse_args(argv)
    try:
        cases = json.loads(args.cases.read_text())['cases']
        if not isinstance(cases, list) or not cases or any(
            not isinstance(case, dict) or not isinstance(case.get('id'), str) or not case['id'].strip()
            for case in cases
        ):
            raise ValueError('maintained task set must contain named cases')
        expected = {case['id'] for case in cases}
        if len(expected) != len(cases):
            raise ValueError('maintained task set contains duplicate case IDs')
        digest = hashlib.sha256(args.cases.read_bytes()).hexdigest()
        baseline = load(args.baseline, expected, digest)
        candidate = load(args.candidate, expected, digest)
        results = [{'id': key, 'baseline': baseline[key]['verdict'], 'candidate': candidate[key]['verdict']} for key in sorted(expected)]
        verdict = 'PASS' if all(case['candidate'] == 'PASS' for case in results) else 'FAIL' if any(case['candidate'] == 'FAIL' for case in results) else 'INCONCLUSIVE'
        print(json.dumps({'verdict': verdict, 'cases': results}, indent=2))
        return {'PASS': 0, 'FAIL': 1, 'INCONCLUSIVE': 2}[verdict]
    except (KeyError, ValueError, OSError, TypeError) as exc:
        print(json.dumps({'verdict': 'FAIL', 'error': str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
