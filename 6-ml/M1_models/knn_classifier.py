#!/usr/bin/env python3
"""M1.03: K-Nearest Neighbors Classifier from Scratch

Implement KNN classification using Euclidean distance.

Problem:
    Given training data X, y and a query point, find the k nearest
    neighbors and return the majority class label.

Functions to implement:
    1. euclidean_distance(a, b) -> distance
       - Compute L2 distance between two points

    2. predict_single(X_train, y_train, x_query, k) -> label
       - Find k nearest neighbors
       - Return majority vote

    3. predict(X_train, y_train, X_test, k) -> labels
       - Predict for multiple query points

Example:
    X_train = [[0, 0], [1, 1], [2, 2], [3, 3]]
    y_train = [0, 0, 1, 1]

    predict(X_train, y_train, [[1.5, 1.5]], k=3)
    # returns [0] or [1] depending on tie-breaking

Edge Cases:
    - Ties in voting (use smallest label or random)
    - k > n_samples (use all samples)
    - Duplicate distances

Complexity:
    Time: O(n * d) per query for n training samples, d features
    Space: O(n) for distance array
"""

import numpy as np
from pathlib import Path
from collections import Counter


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Compute Euclidean (L2) distance between two points.

    Args:
        a: First point
        b: Second point

    Returns:
        Euclidean distance
    """
    # TODO - you fill in here.
    return 0.0


def predict_single(
    X_train: np.ndarray,
    y_train: np.ndarray,
    x_query: np.ndarray,
    k: int
) -> int:
    """Predict class for a single query point.

    Args:
        X_train: Training features, shape (n_samples, n_features)
        y_train: Training labels, shape (n_samples,)
        x_query: Query point, shape (n_features,)
        k: Number of neighbors

    Returns:
        Predicted class label
    """
    # TODO - you fill in here.
    return 0


def predict(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    k: int = 3
) -> np.ndarray:
    """Predict classes for multiple query points.

    Args:
        X_train: Training features
        y_train: Training labels
        X_test: Test features
        k: Number of neighbors

    Returns:
        Predicted labels for each test point
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, y_train, X_test, k=3):
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        predictions = predict(X_train, y_train, X_test, k)
        return predictions.tolist()

    exit(run_tests('knn_classifier_tests.json', test_wrapper))
