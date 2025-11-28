#!/usr/bin/env python3
"""T1.01: Options Quotes → Top-of-Book & NBBO Snapshotter

Ingest per-venue options quotes and publish an NBBO snapshot stream.

Problem:
    Given a CSV of options quotes with per-venue best bid/ask:
    - ts_ns: nanosecond timestamp
    - underlying: underlying symbol
    - occ: OCC option symbol
    - venue: exchange venue
    - bid_px, bid_sz: best bid price and size
    - ask_px, ask_sz: best ask price and size

    For each (time bucket, underlying, occ), compute:
    - Per-venue top-of-book
    - National Best Bid/Offer (NBBO)

    Output snapshots with:
    - ts_bucket_ns: bucketed timestamp
    - underlying, occ
    - nbb_px, nbb_sz: national best bid
    - nbo_px, nbo_sz: national best offer
    - nbb_venue, nbo_venue: venues providing NBB/NBO
    - crossed: True if bid > ask (locked/crossed market)

Edge Cases:
    - Ties across venues (pick first alphabetically)
    - Missing bid or ask side
    - Quotes arriving out of order within bucket
    - Price <= 0 (invalid, skip)

Example:
    Input quotes:
        ts_ns,underlying,occ,venue,bid_px,bid_sz,ask_px,ask_sz
        1732665600123456789,AAPL,AAPL  250124C00180000,CBOE,1.22,15,1.27,22
        1732665600123456789,AAPL,AAPL  250124C00180000,PHLX,1.21,10,1.26,30

    Output (bucket_ms=10):
        ts_bucket_ns,underlying,occ,nbb_px,nbb_sz,nbo_px,nbo_sz,nbb_venue,nbo_venue,crossed
        1732665600120000000,AAPL,AAPL  250124C00180000,1.22,15,1.26,30,CBOE,PHLX,False

Complexity:
    Time: O(n log n) for sorting by time
    Space: O(v) per bucket where v is venues
"""

import csv
from pathlib import Path
from typing import TextIO


def compute_nbbo_snapshots(
    quotes_file: str | TextIO,
    bucket_ms: int = 10
) -> list[dict]:
    """Compute NBBO snapshots from venue quotes.

    Args:
        quotes_file: Path to quotes CSV or file object
        bucket_ms: Time bucket size in milliseconds

    Returns:
        List of NBBO snapshot dictionaries
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests, get_test_data_path

    def test_wrapper(csv_filename: str, bucket_ms: int = 10) -> list[dict]:
        path = Path(__file__).parent / 'test_data' / csv_filename
        return compute_nbbo_snapshots(str(path), bucket_ms)

    exit(run_tests('nbbo_snapshotter_tests.json', test_wrapper))
