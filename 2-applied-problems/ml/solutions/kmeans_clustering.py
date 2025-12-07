"""Solution for M1.04: K-Means Clustering"""
import numpy as np


def initialize_centroids(X: np.ndarray, k: int) -> np.ndarray:
    """Initialize centroids by randomly selecting k points."""
    indices = np.random.choice(len(X), k, replace=False)
    return X[indices].copy()


def assign_clusters(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    """Assign each point to nearest centroid."""
    distances = np.array([[np.sqrt(np.sum((x - c) ** 2)) for c in centroids] for x in X])
    return np.argmin(distances, axis=1)


def update_centroids(X: np.ndarray, labels: np.ndarray, k: int) -> np.ndarray:
    """Update centroids as mean of assigned points."""
    centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        mask = labels == i
        if np.any(mask):
            centroids[i] = X[mask].mean(axis=0)
    return centroids


def fit(X: np.ndarray, k: int, max_iters: int = 100, tol: float = 1e-4) -> tuple[np.ndarray, np.ndarray]:
    """Fit K-means clustering."""
    centroids = initialize_centroids(X, k)

    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)

        if np.allclose(centroids, new_centroids, atol=tol):
            break
        centroids = new_centroids

    return centroids, labels


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X, k, seed=42):
        np.random.seed(seed)
        X = np.array(X)
        centroids, labels = fit(X, k)
        return {'centroids': centroids.tolist(), 'labels': labels.tolist()}

    def cluster_comparator(result, expected):
        result_labels = np.array(result['labels'])
        expected_labels = np.array(expected['labels'])
        mapping = {}
        for r, e in zip(result_labels, expected_labels):
            if r in mapping:
                if mapping[r] != e:
                    return False
            else:
                mapping[r] = e
        return True

    exit(run_tests('kmeans_tests.json', test_wrapper, cluster_comparator))
