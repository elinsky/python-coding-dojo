#!/usr/bin/env python3
"""P3.01: Log File Parser

Parse server log entries and extract structured information using regex.

Problem:
    Given a list of log lines in the format:
    "[TIMESTAMP] LEVEL: message (optional key=value pairs)"

    Extract and return a list of dictionaries with:
    - timestamp: the timestamp string
    - level: log level (INFO, WARN, ERROR, etc.)
    - message: the main message text
    - metadata: dict of any key=value pairs found

Example:
    Input:
        [
            "[2024-01-15 10:30:45] INFO: User logged in (user_id=123 ip=192.168.1.1)",
            "[2024-01-15 10:31:02] ERROR: Database connection failed"
        ]

    Output:
        [
            {
                "timestamp": "2024-01-15 10:30:45",
                "level": "INFO",
                "message": "User logged in",
                "metadata": {"user_id": "123", "ip": "192.168.1.1"}
            },
            {
                "timestamp": "2024-01-15 10:31:02",
                "level": "ERROR",
                "message": "Database connection failed",
                "metadata": {}
            }
        ]

Complexity:
    Time: O(n * m) where n is lines and m is average line length
    Space: O(n) for output list
"""

import re
from pathlib import Path


def parse_logs(log_lines: list[str]) -> list[dict]:
    """Parse log lines into structured dictionaries.

    Args:
        log_lines: List of log line strings

    Returns:
        List of parsed log entry dictionaries
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import run_tests

    exit(run_tests('log_parser_tests.json', parse_logs))
