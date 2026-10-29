"""Green checks for the submitted paid-report contract; product acceptance is separate."""
import unittest
from report import report


class ReportTests(unittest.TestCase):
    def test_paid_report_contract(self):
        value = report()
        self.assertEqual([item['id'] for item in value['invoices']], ['A'])
        self.assertEqual(value['total'], 100)
