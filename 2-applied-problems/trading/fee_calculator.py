#!/usr/bin/env python3
"""T1.08: Fee Schedule Calculator (Maker-Taker, Tiered)

Compute trading fees given per-venue fee tables and trade logs.

Problem:
    Given two inputs:
    A) Fee schedule (JSON):
       {
         "VENUE": {
           "tiers": [
             {"min_adv": 0, "maker": -0.0020, "taker": 0.0030},
             {"min_adv": 1000000, "maker": -0.0025, "taker": 0.0025}
           ]
         }
       }

    B) Trades CSV:
       - ts: timestamp
       - venue: trading venue
       - symbol: instrument symbol
       - side: BUY or SELL
       - qty: trade quantity
       - px: trade price
       - liquidity_flag: M (maker) or T (taker)

    Tasks:
    1. Compute ADV (average daily volume) per venue from trades
    2. Determine correct tier for each venue
    3. Price each fill: fee = qty * px * rate
    4. Aggregate per-venue totals and blended bps

Edge Cases:
    - Unknown liquidity flag (default to taker)
    - Venue not in fee schedule (use default if provided, else skip)
    - Tier boundary edge cases
    - Partial month data

Complexity:
    Time: O(n + v * t) where n is trades, v is venues, t is tiers
    Space: O(v) for per-venue aggregates
"""

import csv
import json
from pathlib import Path
from typing import TextIO


def calculate_fees(
    fee_schedule_file: str | TextIO,
    trades_file: str | TextIO,
    assumed_adv: dict[str, float] | None = None
) -> dict:
    """Calculate trading fees per venue.

    Args:
        fee_schedule_file: Path to fee schedule JSON or file object
        trades_file: Path to trades CSV or file object
        assumed_adv: Optional override for ADV per venue

    Returns:
        Dict with per-venue and total fee summaries
    """
    # TODO - you fill in here.
    return {
        'by_venue': {},
        'total': {
            'gross_value': 0.0,
            'total_fees': 0.0,
            'blended_bps': 0.0
        }
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(fee_file: str, trades_file: str) -> dict:
        base = Path(__file__).parent / 'test_data'
        return calculate_fees(str(base / fee_file), str(base / trades_file))

    exit(run_tests('fee_calculator_tests.json', test_wrapper))
