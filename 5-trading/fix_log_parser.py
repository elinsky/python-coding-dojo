#!/usr/bin/env python3
"""T1.06: FIX Log Parser → Session Stats & Drop-Copy Sanity

Parse FIX (tag-value) logs to verify session health and trading counts.

Problem:
    Given raw FIX log text with messages in tag=value format:
    - Delimiter may be | or SOH (\\x01)
    - Messages may span lines

    Key FIX tags:
    - 8: BeginString (e.g., FIX.4.4)
    - 9: BodyLength
    - 35: MsgType (A=Logon, 5=Logout, 0=Heartbeat, 8=ExecutionReport, D=NewOrderSingle)
    - 34: MsgSeqNum
    - 49: SenderCompID
    - 52: SendingTime
    - 55: Symbol
    - 54: Side (1=Buy, 2=Sell)
    - 32: LastQty (fill qty)
    - 31: LastPx (fill price)
    - 39: OrdStatus (0=New, 1=PartialFill, 2=Filled, 4=Canceled, 8=Rejected)
    - 150: ExecType

    Tasks:
    - Normalize delimiters, parse messages
    - Time-order by tag 52 (SendingTime)
    - Report session stats:
      - logon_count, logout_count
      - heartbeat_count
      - avg_seqnum_gap
      - exec_reports_by_status: {status: count}
      - total_fill_qty, total_fill_value
    - Flag out-of-order seqnums

Edge Cases:
    - Multi-line messages
    - Partial/truncated lines
    - Duplicate seqnums
    - Missing required tags

Complexity:
    Time: O(n * m) where n is messages and m is avg tags per message
    Space: O(n) for parsed messages
"""

import re
from pathlib import Path
from typing import TextIO


def parse_fix_logs(log_file: str | TextIO) -> dict:
    """Parse FIX logs and compute session statistics.

    Args:
        log_file: Path to FIX log file or file object

    Returns:
        Dict with session statistics and flags
    """
    # TODO - you fill in here.
    return {
        'logon_count': 0,
        'logout_count': 0,
        'heartbeat_count': 0,
        'message_count': 0,
        'avg_seqnum_gap': 0.0,
        'exec_reports_by_status': {},
        'total_fill_qty': 0,
        'total_fill_value': 0.0,
        'out_of_order_seqnums': [],
        'warnings': []
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework import run_tests

    def test_wrapper(log_filename: str) -> dict:
        path = Path(__file__).parent / 'test_data' / log_filename
        return parse_fix_logs(str(path))

    exit(run_tests('fix_log_tests.json', test_wrapper))
