"""
Indexing and Slicing Exercises

Problem N1.04 - N1.05
"""
import numpy as np


def last_three_reversed(a: np.ndarray) -> np.ndarray:
    """
    N1.04: Given an array, extract the last 3 elements and reverse them.

    Example:
        Input:  np.arange(10, 100, 10)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]
        Output: [90, 80, 70]

    Args:
        a: Input array

    Returns:
        np.ndarray: Last 3 elements in reverse order
    """
    # TODO - you fill in here
    pass


def replace_even_with_negative_one(a: np.ndarray) -> np.ndarray:
    """
    N1.05: Replace all even numbers with -1 in an array.

    Note: Modify and return a copy, don't modify the original.

    Example:
        Input:  [1, 2, 3, 4, 5, 6]
        Output: [1, -1, 3, -1, 5, -1]

    Args:
        a: Input array of integers

    Returns:
        np.ndarray: Array with even numbers replaced by -1
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test N1.04
    a = np.arange(10, 100, 10)
    result = last_three_reversed(a)
    expected = np.array([90, 80, 70])
    assert result is not None, "N1.04: Function returned None"
    assert np.array_equal(result, expected), f"N1.04: Expected {expected}, got {result}"
    print("N1.04 last_three_reversed: PASSED")

    # Test N1.05
    a = np.array([1, 2, 3, 4, 5, 6])
    result = replace_even_with_negative_one(a)
    expected = np.array([1, -1, 3, -1, 5, -1])
    assert result is not None, "N1.05: Function returned None"
    assert np.array_equal(result, expected), f"N1.05: Expected {expected}, got {result}"
    # Make sure original wasn't modified
    assert np.array_equal(a, np.array([1, 2, 3, 4, 5, 6])), "N1.05: Original array was modified"
    print("N1.05 replace_even_with_negative_one: PASSED")

    print("\nAll indexing/slicing tests passed!")
