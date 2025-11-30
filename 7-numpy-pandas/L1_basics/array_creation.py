"""
Array Creation Exercises

Problem N1.01 - N1.03
"""
import numpy as np


def identity_matrix_3x3() -> np.ndarray:
    """
    N1.01: Create a 3x3 identity matrix.

    Returns:
        np.ndarray: 3x3 identity matrix
    """
    # TODO - you fill in here
    pass


def zeros_with_fifth_one() -> np.ndarray:
    """
    N1.02: Create an array of 10 zeros, then set the 5th value (index 4) to 1.

    Returns:
        np.ndarray: Array of shape (10,) with zeros except index 4 is 1
    """
    # TODO - you fill in here
    pass


def random_array_0_to_1() -> np.ndarray:
    """
    N1.03: Create an array of 10 random numbers between 0 and 1.

    Returns:
        np.ndarray: Array of shape (10,) with random values in [0, 1)
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test N1.01
    result = identity_matrix_3x3()
    expected = np.eye(3)
    assert result is not None, "N1.01: Function returned None"
    assert result.shape == (3, 3), f"N1.01: Expected shape (3,3), got {result.shape}"
    assert np.array_equal(result, expected), "N1.01: Not an identity matrix"
    print("N1.01 identity_matrix_3x3: PASSED")

    # Test N1.02
    result = zeros_with_fifth_one()
    expected = np.zeros(10)
    expected[4] = 1
    assert result is not None, "N1.02: Function returned None"
    assert result.shape == (10,), f"N1.02: Expected shape (10,), got {result.shape}"
    assert np.array_equal(result, expected), f"N1.02: Expected {expected}, got {result}"
    print("N1.02 zeros_with_fifth_one: PASSED")

    # Test N1.03
    result = random_array_0_to_1()
    assert result is not None, "N1.03: Function returned None"
    assert result.shape == (10,), f"N1.03: Expected shape (10,), got {result.shape}"
    assert np.all((result >= 0) & (result < 1)), "N1.03: Values should be in [0, 1)"
    print("N1.03 random_array_0_to_1: PASSED")

    print("\nAll array creation tests passed!")
