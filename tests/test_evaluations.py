import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvaluationReceiptTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)
        self.artifact = self.folder / 'output.md'
        self.artifact.write_text('Actual independently inspected output.\n')
        self.cases = self.folder / 'cases.json'
        self.cases.write_text(json.dumps({'cases': [{'id': 'example'}]}))
        self.baseline = self.folder / 'baseline.json'
        self.candidate = self.folder / 'candidate.json'
        self.record = {
            'revision': 'content-sha256:example', 'evaluator': 'independent evaluator',
            'dataset_sha256': hashlib.sha256(self.cases.read_bytes()).hexdigest(),
            'cases': [{'id': 'example', 'verdict': 'PASS', 'reason': 'Observed original outcome',
                       'artifact': self.artifact.name, 'sha256': hashlib.sha256(self.artifact.read_bytes()).hexdigest()}]
        }
        self.baseline.write_text(json.dumps(self.record))
        self.candidate.write_text(json.dumps(self.record))

    def run_comparison(self):
        return subprocess.run([sys.executable, str(ROOT / 'scripts/compare_evaluations.py'),
                               str(self.baseline), str(self.candidate), '--cases', str(self.cases)],
                              capture_output=True, text=True)

    def test_paired_content_bound_pass(self):
        self.assertEqual(self.run_comparison().returncode, 0)

    def test_changed_output_invalidates_receipt(self):
        self.artifact.write_text('Changed after evaluation')
        self.assertEqual(self.run_comparison().returncode, 1)

    def test_changed_requests_invalidate_comparison(self):
        self.cases.write_text(json.dumps({'cases': [{'id': 'example', 'request': 'new task'}]}))
        self.assertEqual(self.run_comparison().returncode, 1)

    def test_missing_case_cannot_pass(self):
        self.record['cases'] = []
        self.candidate.write_text(json.dumps(self.record))
        self.assertEqual(self.run_comparison().returncode, 1)

    def test_inconclusive_is_not_promoted(self):
        self.record['cases'][0]['verdict'] = 'INCONCLUSIVE'
        self.candidate.write_text(json.dumps(self.record))
        self.assertEqual(self.run_comparison().returncode, 2)

    def test_candidate_regression_cannot_pass(self):
        self.record['cases'][0]['verdict'] = 'FAIL'
        self.candidate.write_text(json.dumps(self.record))
        self.assertEqual(self.run_comparison().returncode, 1)

    def test_empty_task_set_cannot_vacuously_pass(self):
        self.cases.write_text(json.dumps({'cases': []}))
        self.record['cases'] = []
        self.record['dataset_sha256'] = hashlib.sha256(self.cases.read_bytes()).hexdigest()
        for receipt in (self.baseline, self.candidate):
            receipt.write_text(json.dumps(self.record))
        self.assertEqual(self.run_comparison().returncode, 1)

    def test_duplicate_task_ids_cannot_hide_missing_coverage(self):
        self.cases.write_text(json.dumps({'cases': [{'id': 'example'}, {'id': 'example'}]}))
        self.record['dataset_sha256'] = hashlib.sha256(self.cases.read_bytes()).hexdigest()
        for receipt in (self.baseline, self.candidate):
            receipt.write_text(json.dumps(self.record))
        self.assertEqual(self.run_comparison().returncode, 1)
