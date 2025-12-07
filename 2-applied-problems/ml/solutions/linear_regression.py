"""Solution for M1.01: Linear Regression"""
import numpy as np


def fit(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Fit linear regression using normal equation."""
    # Add bias column
    X_bias = np.column_stack([np.ones(len(X)), X])
    # Normal equation: w = (X^T X)^(-1) X^T y
    weights = np.linalg.pinv(X_bias.T @ X_bias) @ X_bias.T @ y
    return weights


def predict(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Predict using fitted weights."""
    X_bias = np.column_stack([np.ones(len(X)), X])
    return X_bias @ weights


if __name__ == '__main__':
    import sys
    from pathlib import Path
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
