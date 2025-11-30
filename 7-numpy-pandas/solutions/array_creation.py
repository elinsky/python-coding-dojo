"""Solutions for Array Creation Exercises"""
import numpy as np


def identity_matrix_3x3() -> np.ndarray:
    return np.eye(3)


def zeros_with_fifth_one() -> np.ndarray:
    arr = np.zeros(10)
    arr[4] = 1
    return arr


def random_array_0_to_1() -> np.ndarray:
    return np.random.random(10)
