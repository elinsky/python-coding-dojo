"""Solution for M1.05: Decision Tree Classifier"""
import numpy as np
from collections import Counter


def entropy(y: np.ndarray) -> float:
    """Compute entropy of label distribution."""
    if len(y) == 0:
        return 0.0
    counter = Counter(y)
    probs = np.array([count / len(y) for count in counter.values()])
    return -np.sum(probs * np.log2(probs + 1e-10))


def information_gain(y: np.ndarray, y_left: np.ndarray, y_right: np.ndarray) -> float:
    """Compute information gain for a split."""
    if len(y_left) == 0 or len(y_right) == 0:
        return 0.0
    n = len(y)
    weighted_entropy = (len(y_left) / n) * entropy(y_left) + (len(y_right) / n) * entropy(y_right)
    return entropy(y) - weighted_entropy


def best_split(X: np.ndarray, y: np.ndarray) -> tuple[int, float] | None:
    """Find the best feature and threshold to split on."""
    best_gain = 0.0
    best_split_info = None

    for feature in range(X.shape[1]):
        sorted_values = np.unique(X[:, feature])
        # Use midpoints between consecutive values as thresholds
        thresholds = (sorted_values[:-1] + sorted_values[1:]) / 2

        for threshold in thresholds:
            left_mask = X[:, feature] <= threshold
            right_mask = ~left_mask

            if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                continue

            gain = information_gain(y, y[left_mask], y[right_mask])
            if gain > best_gain:
                best_gain = gain
                best_split_info = (feature, threshold)

    return best_split_info


def build_tree(X: np.ndarray, y: np.ndarray, max_depth: int = 10, min_samples: int = 2) -> dict:
    """Build decision tree recursively."""
    # Base cases
    if len(y) < min_samples or max_depth == 0 or len(np.unique(y)) == 1:
        return {'leaf': True, 'class': Counter(y).most_common(1)[0][0]}

    split = best_split(X, y)
    if split is None:
        return {'leaf': True, 'class': Counter(y).most_common(1)[0][0]}

    feature, threshold = split
    left_mask = X[:, feature] <= threshold
    right_mask = ~left_mask

    return {
        'leaf': False,
        'feature': feature,
        'threshold': threshold,
        'left': build_tree(X[left_mask], y[left_mask], max_depth - 1, min_samples),
        'right': build_tree(X[right_mask], y[right_mask], max_depth - 1, min_samples)
    }


def predict_single(x: np.ndarray, tree: dict) -> int:
    """Predict class for a single sample."""
    if tree['leaf']:
        return tree['class']
    if x[tree['feature']] <= tree['threshold']:
        return predict_single(x, tree['left'])
    return predict_single(x, tree['right'])


def predict(X: np.ndarray, tree: dict) -> np.ndarray:
    """Predict classes for multiple samples."""
    return np.array([predict_single(x, tree) for x in X])


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, y_train, X_test, max_depth=5):
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        tree = build_tree(X_train, y_train, max_depth)
        predictions = predict(X_test, tree)
        return predictions.tolist()

    exit(run_tests('decision_tree_tests.json', test_wrapper))
