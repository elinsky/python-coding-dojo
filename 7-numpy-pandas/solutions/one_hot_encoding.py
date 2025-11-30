"""Solution for One-Hot Encoding"""
import numpy as np


def one_hot_encode(labels: np.ndarray, n_classes: int) -> np.ndarray:
    result = np.zeros((len(labels), n_classes), dtype=int)
    result[np.arange(len(labels)), labels] = 1
    return result
