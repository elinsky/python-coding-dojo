#!/usr/bin/env python3
"""M3.01: K-Fold Cross Validation from Scratch

Implement k-fold cross validation for model evaluation.

Problem:
    Split data into k folds, train on k-1 folds, evaluate on 1 fold.
    Repeat k times and average the scores.

Functions to implement:
    1. create_folds(n_samples, k) -> list of fold indices
       - Return list of k arrays, each containing indices for that fold

    2. kfold_cross_validate(X, y, model_fn, k=5) -> scores
       - model_fn(X_train, y_train) returns a predict function
       - Return list of k accuracy scores

Example:
    X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    scores = kfold_cross_validate(X, y, model_fn, k=5)
    # scores is list of 5 accuracy values

Edge Cases:
    - n_samples not divisible by k
    - k = n_samples (leave-one-out)

Complexity:
    Time: O(k * model_training_time)
    Space: O(n) for indices
"""

import numpy as np
from pathlib import Path
from typing import Callable


def create_folds(n_samples: int, k: int) -> list[np.ndarray]:
    """Create k fold indices.

    Args:
        n_samples: Total number of samples
        k: Number of folds

    Returns:
        List of k arrays with indices for each fold
    """
    # TODO - you fill in here.
    return []


def kfold_cross_validate(
    X: np.ndarray,
    y: np.ndarray,
    model_fn: Callable,
    k: int = 5
) -> list[float]:
    """Perform k-fold cross validation.

    Args:
        X: Features
        y: Labels
        model_fn: Function(X_train, y_train) -> predict_fn
        k: Number of folds

    Returns:
        List of k accuracy scores
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
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
