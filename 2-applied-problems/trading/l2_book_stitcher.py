#!/usr/bin/env python3
"""T1.05: Order Book L2 Snapshot Stitcher (Depth Builder)

Maintain a 10-level order book from incremental L2 updates.

Problem:
    Given a CSV of L2 incremental updates:
    - ts_ns: nanosecond timestamp
    - symbol: instrument symbol
    - side: BID or ASK
    - level: price level (1-10)
    - px: price
    - sz: size
    - action: UPD (update), DEL (delete), or ADD

    Maintain a 10-level book per symbol and produce snapshots
    after each update that changes the book.

    Output flattened snapshots:
    - ts_ns, symbol
    - bid1_px, bid1_sz, ..., bid10_px, bid10_sz
    - ask1_px, ask1_sz, ..., ask10_px, ask10_sz

Edge Cases:
    - Deletes that leave gaps (compact levels down)
    - Negative sizes (invalid, ignore)
    - Level > 10 (ignore)
    - Level renumbering (handle as updates)

Complexity:
    Time: O(n) for processing updates
    Space: O(s * 20) where s is symbols (10 levels * 2 sides)
"""

import csv
from pathlib import Path
from typing import TextIO
from dataclasses import dataclass, field


@dataclass
class OrderBook:
    """10-level order book for one symbol."""
    bids: list[tuple[float, int]] = field(default_factory=lambda: [(0.0, 0)] * 10)
    asks: list[tuple[float, int]] = field(default_factory=lambda: [(0.0, 0)] * 10)


def process_l2_updates(updates_file: str | TextIO) -> list[dict]:
    """Process L2 updates and produce book snapshots.

    Args:
        updates_file: Path to updates CSV or file object

    Returns:
        List of flattened book snapshot dictionaries
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(csv_filename: str) -> list[dict]:
        path = Path(__file__).parent / 'test_data' / csv_filename
        return process_l2_updates(str(path))

    exit(run_tests('l2_book_tests.json', test_wrapper))
