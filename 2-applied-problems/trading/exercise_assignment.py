#!/usr/bin/env python3
"""T1.11: Options Exercise/Assignment Simulator (EoD)

Simulate end-of-day exercise and assignments given close prices and OCC rules.

Problem:
    Given two inputs:
    A) Positions CSV:
       - acct: account identifier
       - occ: OCC option symbol
       - side: LONG or SHORT
       - qty: position quantity

    B) Close prices CSV:
       - occ: OCC option symbol
       - close_underlying: underlying close price

    OCC Exercise Rules:
    - Options are auto-exercised if ITM by >= $0.01
    - LONG ITM → exercise (acquire/deliver stock)
    - SHORT ITM → assignment (deliver/acquire stock)
    - Call: ITM if close > strike
    - Put: ITM if close < strike

    Tasks:
    1. Parse OCC symbols for strike and type
    2. Determine ITM options
    3. Compute stock position deltas:
       - Long call exercise: +100 shares per contract
       - Long put exercise: -100 shares per contract
       - Short call assignment: -100 shares per contract
       - Short put assignment: +100 shares per contract
    4. Compute P&L impact (intrinsic value)

    Output per account:
    - acct, underlying, stock_delta, pnl_impact

Edge Cases:
    - Penny options (near $0.01 ITM threshold)
    - Zero-bid options (still may be ITM)
    - American vs European style (assume American for equity)
    - Cash-settled index options (no stock delivery)

Complexity:
    Time: O(n + m) where n is positions and m is close prices
    Space: O(a * u) where a is accounts and u is underlyings
"""

import csv
from pathlib import Path
from typing import TextIO


def parse_occ_symbol(occ: str) -> dict:
    """Parse OCC option symbol into components.

    Args:
        occ: OCC symbol like "AAPL  250117C00220000"

    Returns:
        Dict with underlying, expiry, cp_flag, strike
    """
    # TODO - you fill in here.
    return {}


def simulate_exercise_assignment(
    positions_file: str | TextIO,
    closes_file: str | TextIO,
    itm_threshold: float = 0.01,
    contract_size: int = 100
) -> dict:
    """Simulate end-of-day exercise and assignment.

    Args:
        positions_file: Path to positions CSV or file object
        closes_file: Path to close prices CSV or file object
        itm_threshold: Minimum ITM amount for auto-exercise
        contract_size: Shares per contract (usually 100)

    Returns:
        Dict with exercise/assignment results per account
    """
    # TODO - you fill in here.
    return {
        'by_account': [],  # List of {acct, underlying, stock_delta, pnl_impact}
        'summary': {
            'total_exercises': 0,
            'total_assignments': 0,
            'net_stock_delta': {},  # {underlying: delta}
            'total_pnl_impact': 0.0
        }
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(positions_file: str, closes_file: str) -> dict:
        base = Path(__file__).parent / 'test_data'
        return simulate_exercise_assignment(
            str(base / positions_file),
            str(base / closes_file)
        )

    exit(run_tests('exercise_assignment_tests.json', test_wrapper))
