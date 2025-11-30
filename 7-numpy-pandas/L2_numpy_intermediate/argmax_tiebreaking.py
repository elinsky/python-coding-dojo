"""
Argmax with Tie-Breaking

Problem N2.02
"""
import numpy as np


def argmax_per_row(arr: np.ndarray) -> np.ndarray:
    """
    N2.02a: Find the index of the max element per row.

    Args:
        arr: 2D array of shape (m, n)

    Returns:
        np.ndarray: Array of shape (m,) with column index of max per row
    """
    # TODO - you fill in here
    pass


def argmax_per_row_last_tie(arr: np.ndarray) -> np.ndarray:
    """
    N2.02b: Find the index of the max element per row.
    If there are ties, return the LAST index (highest column index).

    Example:
        arr = [[1, 3, 3],
               [2, 2, 1]]
        Output: [2, 1]  (last occurrence of max)

    Args:
        arr: 2D array of shape (m, n)

    Returns:
        np.ndarray: Array of shape (m,) with column index of max per row (last if tied)
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test N2.02a
    arr = np.array([[1, 5, 3],
                    [4, 2, 6],
                    [7, 8, 9]])
    result = argmax_per_row(arr)
    expected = np.array([1, 2, 2])
    assert result is not None, "N2.02a: Function returned None"
    assert np.array_equal(result, expected), f"N2.02a: Expected {expected}, got {result}"
    print("N2.02a argmax_per_row: PASSED")

    # Test N2.02b - ties
    arr = np.array([[1, 3, 3],
                    [2, 2, 1],
                    [5, 5, 5]])
    result = argmax_per_row_last_tie(arr)
    expected = np.array([2, 1, 2])  # last index of max
    assert result is not None, "N2.02b: Function returned None"
    assert np.array_equal(result, expected), f"N2.02b: Expected {expected}, got {result}"
    print("N2.02b argmax_per_row_last_tie: PASSED")

    print("\nAll argmax tests passed!")
