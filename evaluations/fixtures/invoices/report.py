"""Seeded candidate: paid-report implementation that misses an outstanding-report request."""
import json

INVOICES = [
    {'id': 'A', 'status': 'paid', 'amount': 100},
    {'id': 'B', 'status': 'unpaid', 'amount': 25},
    {'id': 'C', 'status': 'unpaid', 'amount': 50},
]


def report():
    paid = [item for item in INVOICES if item['status'] == 'paid']
    return {'invoices': paid, 'total': sum(item['amount'] for item in paid)}


if __name__ == '__main__':
    print(json.dumps(report()))
