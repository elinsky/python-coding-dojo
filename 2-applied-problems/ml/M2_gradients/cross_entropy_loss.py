#!/usr/bin/env python3
"""M2.02: Cross-Entropy Loss and Gradient

Implement binary cross-entropy loss and its gradient.

Problem:
    Binary cross-entropy (log loss) for classification:

    L = -1/n * Σ[y*log(p) + (1-y)*log(1-p)]

    Where p = sigmoid(X @ w + b)

    Gradient with respect to weights:
    dL/dw = 1/n * X^T @ (p - y)
    dL/db = 1/n * Σ(p - y)

Functions to implement:
    1. sigmoid(z) -> activations

    2. binary_cross_entropy(y_true, y_pred) -> loss
       - Compute BCE loss
       - Handle numerical stability (clip predictions)

    3. bce_gradient(X, y_true, y_pred) -> (dw, db)
       - Compute gradients w.r.t. weights and bias

Example:
    y_true = [0, 1, 1, 0]
    y_pred = [0.1, 0.9, 0.8, 0.2]

    loss = binary_cross_entropy(y_true, y_pred)
    # loss ≈ 0.164

Edge Cases:
    - y_pred = 0 or 1 exactly (log undefined)
    - All same class
    - Probabilities outside (0, 1) - clip them

Complexity:
    Time: O(n) for n samples
    Space: O(1) additional
"""

import numpy as np
from pathlib import Path


def sigmoid(z: np.ndarray) -> np.ndarray:
    """Compute sigmoid activation.

    Args:
        z: Input values

    Returns:
        Sigmoid outputs in (0, 1)
    """
    # TODO - you fill in here.
    return np.array([])


def binary_cross_entropy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    eps: float = 1e-15
) -> float:
    """Compute binary cross-entropy loss.

    Args:
        y_true: True labels (0 or 1)
        y_pred: Predicted probabilities
        eps: Small value for numerical stability

    Returns:
        BCE loss value
    """
    # TODO - you fill in here.
    return 0.0


def bce_gradient(
    X: np.ndarray,
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> tuple[np.ndarray, float]:
    """Compute gradient of BCE w.r.t. weights and bias.

    Args:
        X: Features, shape (n, d)
        y_true: True labels
        y_pred: Predicted probabilities

    Returns:
        Tuple of (dw gradient, db gradient)
    """
    # TODO - you fill in here.
    return np.array([]), 0.0


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        loss = binary_cross_entropy(y_true, y_pred)
        return round(loss, 6)

    exit(run_tests('cross_entropy_tests.json', test_wrapper))
