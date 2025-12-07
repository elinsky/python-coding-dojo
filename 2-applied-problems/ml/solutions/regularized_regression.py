"""Solution for M3.02: L1/L2 Regularized Linear Regression"""
import numpy as np


def add_bias(X: np.ndarray) -> np.ndarray:
    """Add column of ones for bias term."""
    return np.column_stack([np.ones(len(X)), X])


def mse_gradient(X: np.ndarray, y: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Compute gradient of MSE loss."""
    n = len(y)
    predictions = X @ weights
    return -1/n * X.T @ (y - predictions)


def fit_ridge(
    X: np.ndarray,
    y: np.ndarray,
    lambda_: float = 1.0,
    lr: float = 0.1,
    epochs: int = 2000
) -> np.ndarray:
    """Fit Ridge (L2) regression."""
    X_bias = add_bias(X)
    weights = np.zeros(X_bias.shape[1])

    for _ in range(epochs):
        gradient = mse_gradient(X_bias, y, weights)
        # Add L2 regularization gradient (don't regularize bias)
        reg_gradient = np.zeros_like(weights)
        reg_gradient[1:] = 2 * lambda_ * weights[1:]
        weights -= lr * (gradient + reg_gradient)

    return weights


def fit_lasso(
    X: np.ndarray,
    y: np.ndarray,
    lambda_: float = 1.0,
    lr: float = 0.1,
    epochs: int = 2000
) -> np.ndarray:
    """Fit Lasso (L1) regression."""
    X_bias = add_bias(X)
    weights = np.zeros(X_bias.shape[1])

    for _ in range(epochs):
        gradient = mse_gradient(X_bias, y, weights)
        # Add L1 regularization gradient (don't regularize bias)
        reg_gradient = np.zeros_like(weights)
        reg_gradient[1:] = lambda_ * np.sign(weights[1:])
        weights -= lr * (gradient + reg_gradient)

    return weights


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, y, method='ridge', lambda_=1.0):
        np.random.seed(42)
        X, y = np.array(X), np.array(y)
        if method == 'ridge':
            return fit_ridge(X, y, lambda_=lambda_).tolist()
        return fit_lasso(X, y, lambda_=lambda_).tolist()

    exit(run_tests('regularization_tests.json', test_wrapper))
