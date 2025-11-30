"""
Custom One-Hot Encoding

Problem N2.04
"""
import numpy as np


def one_hot_encode(labels: np.ndarray, n_classes: int) -> np.ndarray:
    """
    N2.04: Create a one-hot encoded array manually using NumPy (no sklearn).

    Example:
        labels = np.array([1, 3, 2, 1])
        n_classes = 4

        Output: [[0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0],
                 [0, 1, 0, 0]]

    Args:
        labels: 1D array of integer labels (0-indexed)
        n_classes: Total number of classes

    Returns:
        np.ndarray: One-hot encoded array of shape (len(labels), n_classes)
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    labels = np.array([1, 3, 2, 1])
    result = one_hot_encode(labels, n_classes=4)
    expected = np.array([[0, 1, 0, 0],
                         [0, 0, 0, 1],
                         [0, 0, 1, 0],
                         [0, 1, 0, 0]])
    assert result is not None, "N2.04: Function returned None"
    assert result.shape == (4, 4), f"N2.04: Expected shape (4,4), got {result.shape}"
    assert np.array_equal(result, expected), f"N2.04: Expected\n{expected}\ngot\n{result}"
    print("N2.04 one_hot_encode: PASSED")

    # Test with class 0
    labels = np.array([0, 0, 1])
    result = one_hot_encode(labels, n_classes=2)
    expected = np.array([[1, 0],
                         [1, 0],
                         [0, 1]])
    assert np.array_equal(result, expected), f"N2.04 (test 2): Expected\n{expected}\ngot\n{result}"
    print("N2.04 one_hot_encode (test 2): PASSED")

    print("\nAll one-hot tests passed!")
