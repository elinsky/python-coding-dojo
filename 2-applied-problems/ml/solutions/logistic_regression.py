"""Solution for M1.02: Logistic Regression"""
import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    """Compute sigmoid activation."""
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))


def fit(X: np.ndarray, y: np.ndarray, lr: float = 0.1, epochs: int = 1000) -> tuple[np.ndarray, float]:
    """Fit logistic regression using gradient descent."""
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0

    for _ in range(epochs):
        z = X @ weights + bias
        predictions = sigmoid(z)

        dw = (1 / n_samples) * X.T @ (predictions - y)
        db = (1 / n_samples) * np.sum(predictions - y)

        weights -= lr * dw
        bias -= lr * db

    return weights, bias


def predict_proba(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    """Predict probabilities."""
    return sigmoid(X @ weights + bias)


def predict(X: np.ndarray, weights: np.ndarray, bias: float, threshold: float = 0.5) -> np.ndarray:
    """Predict binary labels."""
    return (predict_proba(X, weights, bias) >= threshold).astype(int)


if __name__ == '__main__':
    import sys
    from pathlib import Path
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
