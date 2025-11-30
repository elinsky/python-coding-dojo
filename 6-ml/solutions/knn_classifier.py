"""Solution for M1.03: K-Nearest Neighbors"""
import numpy as np
from collections import Counter


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Compute Euclidean distance."""
    return np.sqrt(np.sum((a - b) ** 2))


def predict_single(X_train: np.ndarray, y_train: np.ndarray, x_query: np.ndarray, k: int) -> int:
    """Predict class for a single query point."""
    distances = [euclidean_distance(x_query, x) for x in X_train]
    k_indices = np.argsort(distances)[:k]
    k_labels = y_train[k_indices]
    # Majority vote (smallest label wins ties)
    counter = Counter(k_labels)
    return min(counter.keys(), key=lambda x: (-counter[x], x))


def predict(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, k: int = 3) -> np.ndarray:
    """Predict classes for multiple query points."""
    return np.array([predict_single(X_train, y_train, x, k) for x in X_test])


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, y_train, X_test, k=3):
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        predictions = predict(X_train, y_train, X_test, k)
        return predictions.tolist()

    exit(run_tests('knn_classifier_tests.json', test_wrapper))
