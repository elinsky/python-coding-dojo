#!/usr/bin/env python3
"""T1.03: Risk Aggregation: Position Greeks → Book Totals

Aggregate per-option Greeks to desk and firm level.

Problem:
    Given a CSV of position Greeks:
    - ts: timestamp
    - book: trading book/desk name
    - underlying: underlying symbol
    - occ: OCC option symbol
    - qty: position quantity (negative = short)
    - delta, gamma, vega, theta: position Greeks

    Produce roll-ups at three levels:
    1. By book
    2. By (book, underlying)
    3. Firm total

    Output three result sets with consistent schemas:
    - level: 'book', 'book_underlying', or 'firm'
    - book: book name (or 'FIRM' for firm total)
    - underlying: underlying (or 'ALL' for book/firm level)
    - total_qty, total_delta, total_gamma, total_vega, total_theta

Edge Cases:
    - Missing Greeks (treat as 0)
    - NaN values (skip row with warning)
    - Duplicated rows (sum them)
    - Inconsistent signs (short calls with positive delta = model bug, warn)

Complexity:
    Time: O(n) for single pass aggregation
    Space: O(b * u) where b is books and u is underlyings
"""

import csv
from pathlib import Path
from typing import TextIO
from collections import defaultdict


def aggregate_greeks(positions_file: str | TextIO) -> dict[str, list[dict]]:
    """Aggregate position Greeks to multiple levels.

    Args:
        positions_file: Path to positions CSV or file object

    Returns:
        Dict with keys 'by_book', 'by_book_underlying', 'firm_total'
        Each value is a list of aggregated row dicts
    """
    # TODO - you fill in here.
    return {
        'by_book': [],
        'by_book_underlying': [],
        'firm_total': []
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(csv_filename: str) -> dict[str, list[dict]]:
        path = Path(__file__).parent / 'test_data' / csv_filename
        return aggregate_greeks(str(path))

    exit(run_tests('risk_aggregation_tests.json', test_wrapper))
