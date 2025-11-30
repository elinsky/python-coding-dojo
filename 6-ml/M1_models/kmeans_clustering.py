#!/usr/bin/env python3
"""M1.04: K-Means Clustering from Scratch

Implement K-means clustering algorithm.

Problem:
    Given data points X and number of clusters k, partition the data
    into k clusters by iteratively:
    1. Assigning points to nearest centroid
    2. Updating centroids to cluster means

Functions to implement:
    1. initialize_centroids(X, k) -> centroids
       - Random initialization: pick k random points from X

    2. assign_clusters(X, centroids) -> labels
       - Assign each point to nearest centroid

    3. update_centroids(X, labels, k) -> new_centroids
       - Compute mean of each cluster

    4. fit(X, k, max_iters=100, tol=1e-4) -> (centroids, labels)
       - Run k-means until convergence or max_iters
       - Convergence: centroids move less than tol

Example:
    X = [[1, 1], [1.5, 1.5], [5, 5], [5.5, 5.5]]
    centroids, labels = fit(X, k=2)
    # labels might be [0, 0, 1, 1] (two clusters)

Edge Cases:
    - Empty cluster (reinitialize that centroid)
    - Random seed for reproducibility
    - Non-convergence

Complexity:
    Time: O(iters * n * k * d) for n points, k clusters, d dims
    Space: O(k * d) for centroids
"""

import numpy as np
from pathlib import Path


def initialize_centroids(X: np.ndarray, k: int) -> np.ndarray:
    """Initialize centroids by randomly selecting k points.

    Args:
        X: Data points, shape (n_samples, n_features)
        k: Number of clusters

    Returns:
        Initial centroids, shape (k, n_features)
    """
    # TODO - you fill in here.
    return np.array([])


def assign_clusters(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    """Assign each point to nearest centroid.

    Args:
        X: Data points, shape (n_samples, n_features)
        centroids: Current centroids, shape (k, n_features)

    Returns:
        Cluster labels, shape (n_samples,)
    """
    # TODO - you fill in here.
    return np.array([])


def update_centroids(
    X: np.ndarray,
    labels: np.ndarray,
    k: int
) -> np.ndarray:
    """Update centroids as mean of assigned points.

    Args:
        X: Data points
        labels: Current cluster assignments
        k: Number of clusters

    Returns:
        Updated centroids, shape (k, n_features)
    """
    # TODO - you fill in here.
    return np.array([])


def fit(
    X: np.ndarray,
    k: int,
    max_iters: int = 100,
    tol: float = 1e-4
) -> tuple[np.ndarray, np.ndarray]:
    """Fit K-means clustering.

    Args:
        X: Data points, shape (n_samples, n_features)
        k: Number of clusters
        max_iters: Maximum iterations
        tol: Convergence tolerance (centroid movement)

    Returns:
        Tuple of (final_centroids, labels)
    """
    # TODO - you fill in here.
    return np.array([]), np.array([])


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, k, seed=42):
        np.random.seed(seed)
        X = np.array(X)
        centroids, labels = fit(X, k)
        return {'centroids': centroids.tolist(), 'labels': labels.tolist()}

    # Custom comparator for clustering (labels may be permuted)
    def cluster_comparator(result, expected):
        if result['labels'] == expected['labels']:
            return True
        # Check if it's a valid permutation
        result_labels = np.array(result['labels'])
        expected_labels = np.array(expected['labels'])
        # Map result labels to expected labels
        mapping = {}
        for r, e in zip(result_labels, expected_labels):
            if r in mapping:
                if mapping[r] != e:
                    return False
            else:
                mapping[r] = e
        return True

    exit(run_tests('kmeans_tests.json', test_wrapper, cluster_comparator))
