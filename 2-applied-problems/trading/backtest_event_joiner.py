#!/usr/bin/env python3
"""T1.12: Backtest Event Joiner (Bars + Ticks + Corporate Actions)

Build a robust event timeline for backtesting from multiple data sources.

Problem:
    Given three inputs:
    A) 1-minute bars CSV:
       - ts: timestamp (minute start)
       - symbol: instrument symbol
       - open, high, low, close: OHLC prices
       - vol: volume

    B) Ticks CSV:
       - ts_ns: nanosecond timestamp
       - symbol: instrument symbol
       - px: trade price
       - qty: trade quantity

    C) Corporate actions CSV:
       - ex_date: ex-dividend/ex-split date
       - symbol: instrument symbol
       - type: SPLIT or DIVIDEND
       - ratio: split ratio (e.g., 2.0 for 2:1) or dividend amount

    Tasks:
    1. Merge all events chronologically
    2. Adjust historical prices/volumes for splits on/after ex_date
    3. Guarantee stable ordering:
       - Ticks before bars at same timestamp
       - Corporate actions at start of day
    4. Emit unified event stream with:
       - event_id: monotonic sequence
       - ts_ns: normalized nanosecond timestamp
       - source: 'tick', 'bar', or 'corp_action'
       - symbol, and source-specific fields

Edge Cases:
    - Timezone normalization
    - Duplicate ticks (same ts, px, qty)
    - Multiple splits/dividends same day
    - Forward vs backward adjustment

Complexity:
    Time: O((n + m + k) log(n + m + k)) for merge sort
    Space: O(n + m + k) for combined events
"""

import csv
from datetime import datetime
from pathlib import Path
from typing import TextIO


def join_backtest_events(
    bars_file: str | TextIO,
    ticks_file: str | TextIO,
    corp_actions_file: str | TextIO,
    adjust_for_splits: bool = True
) -> list[dict]:
    """Join multiple event sources into unified timeline.

    Args:
        bars_file: Path to bars CSV or file object
        ticks_file: Path to ticks CSV or file object
        corp_actions_file: Path to corporate actions CSV or file object
        adjust_for_splits: Whether to adjust prices for splits

    Returns:
        List of unified event dictionaries with monotonic event_id
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(bars: str, ticks: str, corp_actions: str) -> list[dict]:
        base = Path(__file__).parent / 'test_data'
        return join_backtest_events(
            str(base / bars),
            str(base / ticks),
            str(base / corp_actions)
        )

    exit(run_tests('backtest_joiner_tests.json', test_wrapper))
