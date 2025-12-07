"""Solution for M2.02: Cross-Entropy Loss"""
import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    """Compute sigmoid activation."""
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))


def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray, eps: float = 1e-15) -> float:
    """Compute binary cross-entropy loss."""
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def bce_gradient(X: np.ndarray, y_true: np.ndarray, y_pred: np.ndarray) -> tuple[np.ndarray, float]:
    """Compute gradient of BCE."""
    n = len(y_true)
    dw = (1 / n) * X.T @ (y_pred - y_true)
    db = (1 / n) * np.sum(y_pred - y_true)
    return dw, db


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        loss = binary_cross_entropy(y_true, y_pred)
        return round(loss, 6)

    exit(run_tests('cross_entropy_tests.json', test_wrapper))
