"""Solution for M3.01: K-Fold Cross Validation"""
import numpy as np
from typing import Callable


def create_folds(n_samples: int, k: int) -> list[np.ndarray]:
    """Create k fold indices."""
    indices = np.arange(n_samples)
    fold_sizes = np.full(k, n_samples // k)
    fold_sizes[:n_samples % k] += 1

    folds = []
    current = 0
    for fold_size in fold_sizes:
        folds.append(indices[current:current + fold_size])
        current += fold_size

    return folds


def kfold_cross_validate(
    X: np.ndarray,
    y: np.ndarray,
    model_fn: Callable,
    k: int = 5
) -> list[float]:
    """Perform k-fold cross validation."""
    n_samples = len(X)
    folds = create_folds(n_samples, k)
    scores = []

    for i in range(k):
        test_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])

        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        predict_fn = model_fn(X_train, y_train)
        predictions = predict_fn(X_test)

        accuracy = np.mean(predictions == y_test)
        scores.append(accuracy)

    return scores


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, y, k=5):
        np.random.seed(42)
        X = np.array(X)
        y = np.array(y)

        def model_fn(X_train, y_train):
            threshold = np.median(X_train[:, 0])
            return lambda X_test: (X_test[:, 0] > threshold).astype(int)

        scores = kfold_cross_validate(X, y, model_fn, k=k)
        return [round(s, 4) for s in scores]

    exit(run_tests('kfold_tests.json', test_wrapper))
