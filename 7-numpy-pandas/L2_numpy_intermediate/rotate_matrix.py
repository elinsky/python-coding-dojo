"""
Matrix Rotation

Problem N2.03
"""
import numpy as np


def rotate_90_clockwise(matrix: np.ndarray) -> np.ndarray:
    """
    N2.03: Rotate a matrix 90 degrees clockwise (no loops).

    Example:
        Input:  [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

        Output: [[7, 4, 1],
                 [8, 5, 2],
                 [9, 6, 3]]

    Args:
        matrix: 2D array of shape (m, n)

    Returns:
        np.ndarray: Rotated matrix of shape (n, m)
    """
    # TODO - you fill in here (hint: combine transpose and flip)
    pass


# ============ Tests ============
if __name__ == '__main__':
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    result = rotate_90_clockwise(matrix)
    expected = np.array([[7, 4, 1],
                         [8, 5, 2],
                         [9, 6, 3]])
    assert result is not None, "N2.03: Function returned None"
    assert np.array_equal(result, expected), f"N2.03: Expected\n{expected}\ngot\n{result}"
    print("N2.03 rotate_90_clockwise: PASSED")

    # Test non-square
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8]])
    result = rotate_90_clockwise(matrix)
    expected = np.array([[5, 1],
                         [6, 2],
                         [7, 3],
                         [8, 4]])
    assert np.array_equal(result, expected), f"N2.03 (non-square): Expected\n{expected}\ngot\n{result}"
    print("N2.03 rotate_90_clockwise (non-square): PASSED")

    print("\nAll rotation tests passed!")
