#!/usr/bin/env python3
"""M2.01: Gradient Descent Variants

Implement batch, stochastic, and mini-batch gradient descent.

Problem:
    Implement three variants of gradient descent for linear regression:
    - Batch GD: Use all samples for each update
    - Stochastic GD: Use one sample per update
    - Mini-batch GD: Use a batch of samples per update

    Loss: MSE = 1/(2n) * Σ(y - X@w)^2
    Gradient: dw = -1/n * X^T @ (y - X@w)

Functions to implement:
    1. mse_loss(X, y, weights) -> loss
       - Compute mean squared error

    2. mse_gradient(X, y, weights) -> gradient
       - Compute gradient of MSE w.r.t. weights

    3. batch_gd(X, y, lr, epochs) -> weights
       - Standard batch gradient descent

    4. stochastic_gd(X, y, lr, epochs) -> weights
       - Update weights after each sample

    5. minibatch_gd(X, y, lr, epochs, batch_size) -> weights
       - Update weights after each mini-batch

Example:
    X = [[1], [2], [3], [4]]
    y = [2, 4, 6, 8]  # y = 2x

    weights = batch_gd(X, y, lr=0.1, epochs=100)
    # weights converge to [0, 2] (with bias)

Edge Cases:
    - Learning rate too high (divergence)
    - Learning rate too low (slow convergence)
    - Last mini-batch smaller than batch_size

Complexity:
    Batch: O(epochs * n * d)
    SGD: O(epochs * n * d)
    Mini-batch: O(epochs * n/b * b * d) = O(epochs * n * d)
"""

import numpy as np
from pathlib import Path


def add_bias(X: np.ndarray) -> np.ndarray:
    """Add column of ones for bias term."""
    return np.column_stack([np.ones(len(X)), X])


def mse_loss(X: np.ndarray, y: np.ndarray, weights: np.ndarray) -> float:
    """Compute mean squared error loss.

    Args:
        X: Features with bias column, shape (n, d+1)
        y: Targets, shape (n,)
        weights: Weight vector, shape (d+1,)

    Returns:
        MSE loss value
    """
    # TODO - you fill in here.
    return 0.0


def mse_gradient(
    X: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray
) -> np.ndarray:
    """Compute gradient of MSE w.r.t. weights.

    Args:
        X: Features with bias column
        y: Targets
        weights: Current weights

    Returns:
        Gradient vector, shape (d+1,)
    """
    # TODO - you fill in here.
    return np.array([])


def batch_gd(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.01,
    epochs: int = 1000
) -> np.ndarray:
    """Batch gradient descent.

    Args:
        X: Features (without bias), shape (n, d)
        y: Targets
        lr: Learning rate
        epochs: Number of iterations

    Returns:
        Final weights, shape (d+1,)
    """
    # TODO - you fill in here.
    return np.array([])


def stochastic_gd(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.01,
    epochs: int = 100
) -> np.ndarray:
    """Stochastic gradient descent (one sample at a time).

    Args:
        X: Features (without bias)
        y: Targets
        lr: Learning rate
        epochs: Number of passes through data

    Returns:
        Final weights
    """
    # TODO - you fill in here.
    return np.array([])


def minibatch_gd(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.01,
    epochs: int = 100,
    batch_size: int = 32
) -> np.ndarray:
    """Mini-batch gradient descent.

    Args:
        X: Features (without bias)
        y: Targets
        lr: Learning rate
        epochs: Number of passes through data
        batch_size: Number of samples per batch

    Returns:
        Final weights
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, y, variant='batch', lr=0.01, epochs=1000, batch_size=32):
        np.random.seed(42)
        X = np.array(X)
        y = np.array(y)

        if variant == 'batch':
            weights = batch_gd(X, y, lr=lr, epochs=epochs)
        elif variant == 'sgd':
            weights = stochastic_gd(X, y, lr=lr, epochs=epochs)
        else:
            weights = minibatch_gd(X, y, lr=lr, epochs=epochs, batch_size=batch_size)

        # Return predictions on training data
        X_bias = add_bias(X)
        predictions = X_bias @ weights
        return predictions.tolist()

    exit(run_tests('gradient_descent_tests.json', test_wrapper))
