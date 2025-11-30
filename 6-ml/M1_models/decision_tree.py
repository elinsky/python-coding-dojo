#!/usr/bin/env python3
"""M1.05: Decision Tree Classifier from Scratch

Implement a binary decision tree classifier using information gain.

Problem:
    Build a decision tree by recursively finding the best feature and
    threshold to split on, using information gain (reduction in entropy).

    Entropy: H(S) = -Σ p_i * log2(p_i)
    Information Gain: IG = H(parent) - weighted_avg(H(children))

Functions to implement:
    1. entropy(y) -> float
       - Compute entropy of label distribution

    2. information_gain(y, y_left, y_right) -> float
       - Compute IG for a split

    3. best_split(X, y) -> (feature_idx, threshold)
       - Find best feature and threshold to split on
       - Try all features and all unique values as thresholds

    4. build_tree(X, y, max_depth) -> tree node
       - Recursively build tree
       - Stop at max_depth or pure node

    5. predict_single(x, tree) -> label

    6. predict(X, tree) -> labels

Tree node structure (dict):
    {'leaf': True, 'class': label}
    or
    {'leaf': False, 'feature': idx, 'threshold': val,
     'left': subtree, 'right': subtree}

Example:
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]  # AND gate

    tree = build_tree(X, y, max_depth=3)
    predict([[1, 1]], tree)  # returns [1]

Edge Cases:
    - Pure node (all same label)
    - Single sample
    - No valid splits (return majority)

Complexity:
    Time: O(n * d * n * log(n)) per level for n samples, d features
    Space: O(depth) for recursion
"""

import numpy as np
from pathlib import Path
from collections import Counter


def entropy(y: np.ndarray) -> float:
    """Compute entropy of label distribution.

    Args:
        y: Labels

    Returns:
        Entropy value (0 if pure, higher if mixed)
    """
    # TODO - you fill in here.
    return 0.0


def information_gain(
    y: np.ndarray,
    y_left: np.ndarray,
    y_right: np.ndarray
) -> float:
    """Compute information gain for a split.

    Args:
        y: Parent labels
        y_left: Left child labels
        y_right: Right child labels

    Returns:
        Information gain
    """
    # TODO - you fill in here.
    return 0.0


def best_split(X: np.ndarray, y: np.ndarray) -> tuple[int, float] | None:
    """Find the best feature and threshold to split on.

    Args:
        X: Features, shape (n_samples, n_features)
        y: Labels, shape (n_samples,)

    Returns:
        Tuple of (feature_index, threshold) or None if no valid split
    """
    # TODO - you fill in here.
    return None


def build_tree(
    X: np.ndarray,
    y: np.ndarray,
    max_depth: int = 10,
    min_samples: int = 2
) -> dict:
    """Build decision tree recursively.

    Args:
        X: Features
        y: Labels
        max_depth: Maximum tree depth
        min_samples: Minimum samples to split

    Returns:
        Tree node (dict)
    """
    # TODO - you fill in here.
    return {'leaf': True, 'class': 0}


def predict_single(x: np.ndarray, tree: dict) -> int:
    """Predict class for a single sample.

    Args:
        x: Single sample features
        tree: Trained tree

    Returns:
        Predicted class
    """
    # TODO - you fill in here.
    return 0


def predict(X: np.ndarray, tree: dict) -> np.ndarray:
    """Predict classes for multiple samples.

    Args:
        X: Features
        tree: Trained tree

    Returns:
        Predicted classes
    """
    # TODO - you fill in here.
    return np.array([])


if __name__ == '__main__':
    import sys
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
