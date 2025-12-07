#!/usr/bin/env python3
"""M1.01: Linear Regression from Scratch

Implement linear regression using the closed-form solution (normal equation).

Problem:
    Given training data X (features) and y (targets), compute the optimal
    weights using the normal equation:

    w = (X^T X)^(-1) X^T y

    Then use the weights to predict on new data.

Functions to implement:
    1. fit(X, y) -> weights
       - Add bias term (column of 1s) to X
       - Compute weights using normal equation
       - Return weights array (including bias as first element)

    2. predict(X, weights) -> predictions
       - Add bias term to X
       - Return X @ weights

Example:
    X_train = [[1], [2], [3]]  # Single feature
    y_train = [2, 4, 6]        # y = 2x

    weights = fit(X_train, y_train)
    # weights ≈ [0, 2] (bias ≈ 0, slope ≈ 2)

    predict([[4], [5]], weights)
    # returns ≈ [8, 10]

Edge Cases:
    - Single feature vs multiple features
    - Perfect fit vs noisy data
    - Near-singular X^T X (add small regularization if needed)

Complexity:
    Time: O(n*d^2 + d^3) for n samples, d features (matrix inversion)
    Space: O(d^2) for X^T X matrix
"""

import numpy as np
from pathlib import Path


def fit(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Fit linear regression using normal equation.

    Args:
        X: Training features, shape (n_samples, n_features)
        y: Training targets, shape (n_samples,)

    Returns:
        Weights array, shape (n_features + 1,) with bias as first element
    """
    # TODO - you fill in here.
    return np.array([])


def predict(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Predict using fitted weights.

    Args:
        X: Features, shape (n_samples, n_features)
        weights: Weight array from fit(), shape (n_features + 1,)

    Returns:
        Predictions, shape (n_samples,)
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, y_train, X_test):
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        weights = fit(X_train, y_train)
        predictions = predict(X_test, weights)
        return predictions.tolist()

    exit(run_tests('linear_regression_tests.json', test_wrapper))
