#!/usr/bin/env python3
"""T1.04: Execution Log Parser → P&L Explain (Price vs. Slippage vs. Fees)

Break down intraday realized P&L per instrument.

Problem:
    Given two inputs:
    A) Fills CSV:
       - ts_ns: nanosecond timestamp
       - venue: execution venue
       - symbol: instrument symbol
       - side: BUY or SELL
       - qty: fill quantity
       - px: fill price
       - fee: fee amount (negative = cost, positive = rebate)

    B) Close prices CSV:
       - symbol: instrument symbol
       - close_px: end-of-day close price

    Compute realized P&L decomposition:
    - mark_to_close: Σ(side_sign * qty * (close_px - fill_px))
    - fees: Σ(fee)
    - total_pnl: mark_to_close + fees

    Aggregate per symbol and total.

Edge Cases:
    - Partial fills (just sum them)
    - Short sells (side=SELL with no prior buy = short)
    - Missing close price → skip with warning
    - Empty fills → return empty result

Complexity:
    Time: O(n + m) where n is fills and m is close prices
    Space: O(s) where s is unique symbols
"""

import csv
from pathlib import Path
from typing import TextIO


def explain_pnl(
    fills_file: str | TextIO,
    closes_file: str | TextIO
) -> dict:
    """Compute P&L explain from fills and close prices.

    Args:
        fills_file: Path to fills CSV or file object
        closes_file: Path to close prices CSV or file object

    Returns:
        Dict with:
        - by_symbol: list of per-symbol P&L dicts
        - total: aggregate P&L dict
        - warnings: list of warning messages
    """
    # TODO - you fill in here.
    return {
        'by_symbol': [],
        'total': {'mark_to_close': 0.0, 'fees': 0.0, 'total_pnl': 0.0},
        'warnings': []
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(fills_file: str, closes_file: str) -> dict:
        base = Path(__file__).parent / 'test_data'
        return explain_pnl(str(base / fills_file), str(base / closes_file))

    exit(run_tests('pnl_explain_tests.json', test_wrapper))
