#!/usr/bin/env python3
"""P2.01: Flatten Nested JSON

Transform a nested JSON structure into a flat dictionary with dot-notation keys.

Problem:
    Given a nested dictionary, flatten it so that nested keys are joined with dots.
    Arrays should use numeric indices in the key path.

Example:
    Input:
        {
            "name": "John",
            "address": {
                "city": "NYC",
                "zip": "10001"
            },
            "phones": ["555-1234", "555-5678"]
        }

    Output:
        {
            "name": "John",
            "address.city": "NYC",
            "address.zip": "10001",
            "phones.0": "555-1234",
            "phones.1": "555-5678"
        }

Complexity:
    Time: O(n) where n is total number of leaf values
    Space: O(n) for the output dictionary
"""

from pathlib import Path


def flatten_json(data: dict) -> dict:
    """Flatten a nested dictionary into dot-notation keys.

    Args:
        data: Nested dictionary to flatten

    Returns:
        Flat dictionary with dot-notation keys
    """
    # TODO - you fill in here.
    return {}


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import run_tests

    exit(run_tests('json_flatten_tests.json', flatten_json))
