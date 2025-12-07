#!/usr/bin/env python3
"""T1.07: Options Surface Cleaner → Sparse Grid Interpolator

Build a same-day IV surface from noisy quotes.

Problem:
    Given a CSV of IV data points:
    - ts: timestamp
    - underlying: underlying symbol
    - days: days to expiry
    - strike: option strike
    - cp_flag: C or P
    - iv: implied volatility
    - bid_ask_width: optional bid-ask spread width

    Tasks:
    1. Deduplicate by (days, strike, cp_flag):
       - Keep lowest bid_ask_width if available, else latest timestamp
    2. Enforce monotonic ATM term structure (tolerance-based)
    3. Drop outliers (e.g., IV < 0.01 or > 5.0)
    4. Interpolate a dense grid:
       - days: [7, 14, 21, 30, 60, 90]
       - strikes: 50 points around spot in 2% steps
    5. Output the interpolated grid

Edge Cases:
    - Missing wings (extrapolate flat or skip)
    - Single call or put side only
    - Insufficient data for interpolation

Complexity:
    Time: O(n log n) for sorting + O(g) for grid interpolation
    Space: O(n + g) where g is grid size
"""

import csv
from pathlib import Path
from typing import TextIO


def clean_and_interpolate_surface(
    iv_file: str | TextIO,
    spot: float,
    min_iv: float = 0.01,
    max_iv: float = 5.0
) -> list[dict]:
    """Clean IV data and interpolate a dense surface grid.

    Args:
        iv_file: Path to IV data CSV or file object
        spot: Current underlying spot price
        min_iv: Minimum valid IV (filter below)
        max_iv: Maximum valid IV (filter above)

    Returns:
        List of interpolated grid point dictionaries
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(csv_filename: str, spot: float) -> list[dict]:
        path = Path(__file__).parent / 'test_data' / csv_filename
        return clean_and_interpolate_surface(str(path), spot)

    exit(run_tests('iv_surface_tests.json', test_wrapper))
