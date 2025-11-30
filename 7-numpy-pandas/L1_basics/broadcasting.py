"""
Broadcasting Exercises

Problem N1.06
"""
import numpy as np


def add_1d_to_each_row(arr_2d: np.ndarray, arr_1d: np.ndarray) -> np.ndarray:
    """
    N1.06: Add a 1D array to each row of a 2D array.

    Example:
        arr_2d = [[1, 1, 1],
                  [2, 2, 2],
                  [3, 3, 3]]
        arr_1d = [1, 2, 3]

        Output = [[2, 3, 4],
                  [3, 4, 5],
                  [4, 5, 6]]

    Args:
        arr_2d: 2D array of shape (n, m)
        arr_1d: 1D array of shape (m,)

    Returns:
        np.ndarray: Result of adding arr_1d to each row of arr_2d
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test N1.06
    arr_2d = np.array([[1, 1, 1],
                       [2, 2, 2],
                       [3, 3, 3]])
    arr_1d = np.array([1, 2, 3])
    result = add_1d_to_each_row(arr_2d, arr_1d)
    expected = np.array([[2, 3, 4],
                         [3, 4, 5],
                         [4, 5, 6]])
    assert result is not None, "N1.06: Function returned None"
    assert np.array_equal(result, expected), f"N1.06: Expected\n{expected}\ngot\n{result}"
    print("N1.06 add_1d_to_each_row: PASSED")

    # Test with different values
    arr_2d = np.ones((3, 3))
    arr_1d = np.array([10, 20, 30])
    result = add_1d_to_each_row(arr_2d, arr_1d)
    expected = np.array([[11, 21, 31],
                         [11, 21, 31],
                         [11, 21, 31]])
    assert np.array_equal(result, expected), f"N1.06 (test 2): Expected\n{expected}\ngot\n{result}"
    print("N1.06 add_1d_to_each_row (test 2): PASSED")

    print("\nAll broadcasting tests passed!")
