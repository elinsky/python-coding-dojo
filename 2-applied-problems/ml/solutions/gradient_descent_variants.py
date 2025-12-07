"""Solution for M2.01: Gradient Descent Variants"""
import numpy as np


def add_bias(X: np.ndarray) -> np.ndarray:
    """Add column of ones for bias term."""
    return np.column_stack([np.ones(len(X)), X])


def mse_loss(X: np.ndarray, y: np.ndarray, weights: np.ndarray) -> float:
    """Compute mean squared error loss."""
    predictions = X @ weights
    return np.mean((y - predictions) ** 2) / 2


def mse_gradient(X: np.ndarray, y: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Compute gradient of MSE."""
    n = len(y)
    predictions = X @ weights
    return -1/n * X.T @ (y - predictions)


def batch_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 1000) -> np.ndarray:
    """Batch gradient descent."""
    X_bias = add_bias(X)
    weights = np.zeros(X_bias.shape[1])

    for _ in range(epochs):
        gradient = mse_gradient(X_bias, y, weights)
        weights -= lr * gradient

    return weights


def stochastic_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 100) -> np.ndarray:
    """Stochastic gradient descent."""
    X_bias = add_bias(X)
    weights = np.zeros(X_bias.shape[1])
    n = len(y)

    for _ in range(epochs):
        indices = np.random.permutation(n)
        for i in indices:
            xi = X_bias[i:i+1]
            yi = y[i:i+1]
            gradient = mse_gradient(xi, yi, weights)
            weights -= lr * gradient

    return weights


def minibatch_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 100, batch_size: int = 32) -> np.ndarray:
    """Mini-batch gradient descent."""
    X_bias = add_bias(X)
    weights = np.zeros(X_bias.shape[1])
    n = len(y)

    for _ in range(epochs):
        indices = np.random.permutation(n)
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            batch_idx = indices[start:end]
            Xi = X_bias[batch_idx]
            yi = y[batch_idx]
            gradient = mse_gradient(Xi, yi, weights)
            weights -= lr * gradient

    return weights


if __name__ == '__main__':
    import sys
    from pathlib import Path
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

        X_bias = add_bias(X)
        predictions = X_bias @ weights
        return predictions.tolist()

    exit(run_tests('gradient_descent_tests.json', test_wrapper))
