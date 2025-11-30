"""
Distance Matrix

Problem N2.01
"""
import numpy as np


def pairwise_euclidean_distance(points: np.ndarray) -> np.ndarray:
    """
    N2.01: Compute the pairwise Euclidean distance matrix.

    Given n points in d dimensions, return an n x n matrix where
    entry (i, j) is the Euclidean distance between point i and point j.

    Example:
        points = np.array([[1, 2], [3, 4], [5, 6]])
        Output: [[0.0, 2.83, 5.66],
                 [2.83, 0.0, 2.83],
                 [5.66, 2.83, 0.0]]  (approximately)

    Args:
        points: Array of shape (n, d) where n is number of points, d is dimensions

    Returns:
        np.ndarray: Distance matrix of shape (n, n)
    """
    # TODO - you fill in here (try to avoid explicit loops)
    pass


# ============ Tests ============
if __name__ == '__main__':
    points = np.array([[1, 2], [3, 4], [5, 6]])
    result = pairwise_euclidean_distance(points)

    assert result is not None, "N2.01: Function returned None"
    assert result.shape == (3, 3), f"N2.01: Expected shape (3,3), got {result.shape}"

    # Check diagonal is zeros
    assert np.allclose(np.diag(result), 0), "N2.01: Diagonal should be zeros"

    # Check symmetry
    assert np.allclose(result, result.T), "N2.01: Matrix should be symmetric"

    # Check specific distance
    expected_01 = np.sqrt((3-1)**2 + (4-2)**2)  # sqrt(8) ≈ 2.83
    assert np.isclose(result[0, 1], expected_01), f"N2.01: Distance [0,1] should be {expected_01}"

    print("N2.01 pairwise_euclidean_distance: PASSED")
