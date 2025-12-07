#!/usr/bin/env python3
"""Test framework for practical programming problems.

Similar to EPI's generic_test but designed for file-based and data processing problems.
"""

import json
import sys
from pathlib import Path
from typing import Any, Callable


def load_test_cases(test_file: str) -> list[dict]:
    """Load test cases from a JSON file.

    Args:
        test_file: Path to test cases JSON file (relative to test_data/)

    Returns:
        List of test case dictionaries with 'input' and 'expected' keys
    """
    test_data_dir = Path(__file__).parent.parent / 'test_data'
    test_path = test_data_dir / test_file

    if not test_path.exists():
        raise FileNotFoundError(f"Test file not found: {test_path}")

    with open(test_path, 'r') as f:
        return json.load(f)


def run_tests(
    test_file: str,
    solution_func: Callable,
    comparator: Callable[[Any, Any], bool] | None = None
) -> int:
    """Run all test cases against a solution function.

    Args:
        test_file: Path to test cases JSON file
        solution_func: Function to test
        comparator: Optional custom comparison function (default: ==)

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    if comparator is None:
        comparator = lambda a, b: a == b

    test_cases = load_test_cases(test_file)
    passed = 0
    failed = 0

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case['input']
        expected = test_case['expected']
        description = test_case.get('description', f'Test case {i}')

        try:
            # Handle different input formats
            # Use 'args' key for positional args, 'kwargs' for keyword args
            # Otherwise pass input directly as single argument
            if isinstance(input_data, dict) and 'args' in input_data:
                result = solution_func(*input_data['args'], **input_data.get('kwargs', {}))
            elif isinstance(input_data, dict) and 'kwargs' in input_data:
                result = solution_func(**input_data['kwargs'])
            else:
                # Pass input directly as single argument
                result = solution_func(input_data)

            if comparator(result, expected):
                print(f"✓ {description}")
                passed += 1
            else:
                print(f"✗ {description}")
                print(f"  Input: {input_data}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
                failed += 1

        except Exception as e:
            print(f"✗ {description}")
            print(f"  Input: {input_data}")
            print(f"  Error: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")

    return 0 if failed == 0 else 1


def get_test_data_path(filename: str) -> Path:
    """Get absolute path to a file in the test_data directory.

    Args:
        filename: Name of the file in test_data/

    Returns:
        Absolute Path to the file
    """
    return Path(__file__).parent.parent / 'test_data' / filename
