"""Solution for Matrix Rotation"""
import numpy as np


def rotate_90_clockwise(matrix: np.ndarray) -> np.ndarray:
    # Transpose then flip horizontally
    return np.flipud(matrix.T)
    # Alternative: return np.rot90(matrix, k=-1)
