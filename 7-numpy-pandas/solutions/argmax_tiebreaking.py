"""Solution for Argmax with Tie-Breaking"""
import numpy as np


def argmax_per_row(arr: np.ndarray) -> np.ndarray:
    return np.argmax(arr, axis=1)


def argmax_per_row_last_tie(arr: np.ndarray) -> np.ndarray:
    # Flip columns, find argmax, then convert back to original index
    flipped = np.fliplr(arr)
    return arr.shape[1] - 1 - np.argmax(flipped, axis=1)
