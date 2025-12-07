#!/usr/bin/env python3
"""M1.02: Logistic Regression from Scratch

Implement binary logistic regression using gradient descent.

Problem:
    Given training data X (features) and y (binary labels 0/1), train a
    logistic regression classifier using gradient descent.

    Model: P(y=1|x) = sigmoid(x @ w + b) = 1 / (1 + exp(-(x @ w + b)))

    Loss: Binary cross-entropy
    L = -1/n * Σ[y*log(p) + (1-y)*log(1-p)]

    Gradients:
    dw = 1/n * X^T @ (predictions - y)
    db = 1/n * Σ(predictions - y)

Functions to implement:
    1. sigmoid(z) -> activations

    2. fit(X, y, lr=0.1, epochs=1000) -> (weights, bias)
       - Initialize weights to zeros
       - Gradient descent loop
       - Return final weights and bias

    3. predict_proba(X, weights, bias) -> probabilities

    4. predict(X, weights, bias, threshold=0.5) -> binary predictions

Example:
    X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_train = [0, 0, 0, 1]  # AND gate

    weights, bias = fit(X_train, y_train)
    predict([[1, 1]], weights, bias)  # returns [1]

Edge Cases:
    - Linearly separable vs non-separable data
    - Numerical stability in log (clip probabilities)
    - Learning rate tuning

Complexity:
    Time: O(epochs * n * d) for n samples, d features
    Space: O(d) for weights
"""

import numpy as np
from pathlib import Path


def sigmoid(z: np.ndarray) -> np.ndarray:
    """Compute sigmoid activation.

    Args:
        z: Input values

    Returns:
        Sigmoid activations in range (0, 1)
    """
    # TODO - you fill in here.
    return np.array([])


def fit(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.1,
    epochs: int = 1000
) -> tuple[np.ndarray, float]:
    """Fit logistic regression using gradient descent.

    Args:
        X: Training features, shape (n_samples, n_features)
        y: Training labels (0 or 1), shape (n_samples,)
        lr: Learning rate
        epochs: Number of gradient descent iterations

    Returns:
        Tuple of (weights, bias)
    """
    # TODO - you fill in here.
    return np.array([]), 0.0


def predict_proba(
    X: np.ndarray,
    weights: np.ndarray,
    bias: float
) -> np.ndarray:
    """Predict probabilities.

    Args:
        X: Features, shape (n_samples, n_features)
        weights: Learned weights
        bias: Learned bias

    Returns:
        Probabilities, shape (n_samples,)
    """
    # TODO - you fill in here.
    return np.array([])


def predict(
    X: np.ndarray,
    weights: np.ndarray,
    bias: float,
    threshold: float = 0.5
) -> np.ndarray:
    """Predict binary labels.

    Args:
        X: Features, shape (n_samples, n_features)
        weights: Learned weights
        bias: Learned bias
        threshold: Classification threshold

    Returns:
        Binary predictions (0 or 1), shape (n_samples,)
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, y_train, X_test, lr=0.1, epochs=1000):
        np.random.seed(42)
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        weights, bias = fit(X_train, y_train, lr=lr, epochs=epochs)
        predictions = predict(X_test, weights, bias)
        return predictions.tolist()

    exit(run_tests('logistic_regression_tests.json', test_wrapper))
