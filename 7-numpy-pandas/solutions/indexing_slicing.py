"""Solutions for Indexing and Slicing Exercises"""
import numpy as np


def last_three_reversed(a: np.ndarray) -> np.ndarray:
    return a[-3:][::-1]


def replace_even_with_negative_one(a: np.ndarray) -> np.ndarray:
    result = a.copy()
    result[result % 2 == 0] = -1
    return result
