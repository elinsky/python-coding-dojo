# ML problems test framework
import json
import numpy as np
from pathlib import Path
from typing import Any, Callable


def load_test_cases(test_file: str) -> list[dict]:
    """Load test cases from a JSON file in ML test_data."""
    test_data_dir = Path(__file__).parent.parent / 'test_data'
    test_path = test_data_dir / test_file

    if not test_path.exists():
        raise FileNotFoundError(f"Test file not found: {test_path}")

    with open(test_path, 'r') as f:
        return json.load(f)


def get_test_data_path(filename: str) -> Path:
    """Get path to a file in ML test_data directory."""
    return Path(__file__).parent.parent / 'test_data' / filename


def arrays_close(a: Any, b: Any, rtol: float = 1e-4, atol: float = 1e-6) -> bool:
    """Compare arrays/values with tolerance for floating point."""
    if isinstance(a, (list, tuple)):
        a = np.array(a)
    if isinstance(b, (list, tuple)):
        b = np.array(b)

    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        return np.allclose(a, b, rtol=rtol, atol=atol)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return np.isclose(a, b, rtol=rtol, atol=atol)
    else:
        return a == b


def run_tests(
    test_file: str,
    solution_func: Callable,
    comparator: Callable[[Any, Any], bool] | None = None
) -> int:
    """Run all test cases against a solution function."""
    if comparator is None:
        comparator = arrays_close

    test_cases = load_test_cases(test_file)
    passed = 0
    failed = 0

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case['input']
        expected = test_case['expected']
        description = test_case.get('description', f'Test case {i}')

        try:
            if isinstance(input_data, dict) and 'args' in input_data:
                result = solution_func(*input_data['args'], **input_data.get('kwargs', {}))
            elif isinstance(input_data, dict) and 'kwargs' in input_data:
                result = solution_func(**input_data['kwargs'])
            else:
                result = solution_func(input_data)

            if comparator(result, expected):
                print(f"✓ {description}")
                passed += 1
            else:
                print(f"✗ {description}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
                failed += 1

        except Exception as e:
            print(f"✗ {description}")
            print(f"  Error: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")
    return 0 if failed == 0 else 1


__all__ = ['run_tests', 'load_test_cases', 'get_test_data_path', 'arrays_close']
