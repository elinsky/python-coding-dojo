#!/usr/bin/env python3
"""M3.02: L1/L2 Regularized Linear Regression

Implement Ridge (L2) and Lasso (L1) regularization.

Problem:
    Add regularization penalty to linear regression:

    Ridge (L2): L = MSE + lambda * ||w||_2^2
    Lasso (L1): L = MSE + lambda * ||w||_1

    Gradients (don't regularize bias):
    Ridge: dw = dw_mse + 2*lambda*w
    Lasso: dw = dw_mse + lambda*sign(w)

Functions to implement:
    1. fit_ridge(X, y, lambda_, lr, epochs) -> weights
    2. fit_lasso(X, y, lambda_, lr, epochs) -> weights

Example:
    # High lambda -> weights shrink toward 0
    w_ridge = fit_ridge(X, y, lambda_=1.0)
    w_lasso = fit_lasso(X, y, lambda_=1.0)
    # Lasso tends to produce sparser weights

Edge Cases:
    - lambda=0 (no regularization)
    - Very high lambda (weights -> 0)

Complexity:
    Time: O(epochs * n * d)
    Space: O(d)
"""

import numpy as np
from pathlib import Path


def fit_ridge(
    X: np.ndarray,
    y: np.ndarray,
    lambda_: float = 1.0,
    lr: float = 0.01,
    epochs: int = 1000
) -> np.ndarray:
    """Fit Ridge (L2) regression.

    Args:
        X: Features (without bias)
        y: Targets
        lambda_: Regularization strength
        lr: Learning rate
        epochs: Iterations

    Returns:
        Weights with bias as first element
    """
    # TODO - you fill in here.
    return np.array([])


def fit_lasso(
    X: np.ndarray,
    y: np.ndarray,
    lambda_: float = 1.0,
    lr: float = 0.01,
    epochs: int = 1000
) -> np.ndarray:
    """Fit Lasso (L1) regression.

    Args:
        X: Features (without bias)
        y: Targets
        lambda_: Regularization strength
        lr: Learning rate
        epochs: Iterations

    Returns:
        Weights with bias as first element
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, y, method='ridge', lambda_=1.0):
        np.random.seed(42)
        X, y = np.array(X), np.array(y)
        if method == 'ridge':
            return fit_ridge(X, y, lambda_=lambda_).tolist()
        return fit_lasso(X, y, lambda_=lambda_).tolist()

    exit(run_tests('regularization_tests.json', test_wrapper))
