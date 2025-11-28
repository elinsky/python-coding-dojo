#!/usr/bin/env python3
"""T1.10: OUCH/ITCH-like Binary Parser → Trade/Quote Tape

Parse a binary equity feed into a trade/quote tape.

Problem:
    Given a raw binary file with messages in this format:

    Header (per message):
    - seq: uint32 (4 bytes, big-endian) - sequence number
    - ts_ns: uint64 (8 bytes, big-endian) - nanosecond timestamp
    - type: char (1 byte) - message type

    Message Types:
    'T' - Trade:
      - px: int32 (4 bytes, price * 10000)
      - qty: uint32 (4 bytes)
      - symbol: 8 bytes (space-padded)

    'Q' - Quote:
      - bid: int32 (4 bytes, price * 10000)
      - ask: int32 (4 bytes, price * 10000)
      - bsz: uint32 (4 bytes, bid size)
      - asz: uint32 (4 bytes, ask size)
      - symbol: 8 bytes (space-padded)

    Tasks:
    1. Decode binary stream
    2. Maintain per-symbol running state:
       - last_px, last_qty (from trades)
       - bid, bsz, ask, asz (from quotes)
    3. Emit CSV tape after each message:
       ts_ns, symbol, last_px, last_qty, bid, bsz, ask, asz
    4. Validate sequence monotonicity, count gaps

Edge Cases:
    - Padding zeros in symbol (strip them)
    - Negative prices (invalid, skip message)
    - Truncated messages at end of file
    - Unknown message types (skip)

Complexity:
    Time: O(n) for linear scan
    Space: O(s) where s is unique symbols
"""

import struct
from pathlib import Path
from typing import BinaryIO


def parse_binary_feed(binary_file: str | BinaryIO) -> dict:
    """Parse binary feed into trade/quote tape.

    Args:
        binary_file: Path to binary file or binary file object

    Returns:
        Dict with tape (list of records), sequence gaps, and stats
    """
    # TODO - you fill in here.
    return {
        'tape': [],  # List of {ts_ns, symbol, last_px, last_qty, bid, bsz, ask, asz}
        'sequence_gaps': [],  # List of (expected, actual) tuples
        'stats': {
            'total_messages': 0,
            'trade_count': 0,
            'quote_count': 0,
            'invalid_count': 0
        }
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(bin_filename: str) -> dict:
        path = Path(__file__).parent / 'test_data' / bin_filename
        return parse_binary_feed(str(path))

    exit(run_tests('binary_feed_tests.json', test_wrapper))
