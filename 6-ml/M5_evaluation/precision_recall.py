#!/usr/bin/env python3
"""M5.02: Precision-Recall Curve from Scratch

Implement precision-recall curve computation.

Problem:
    Precision = TP / (TP + FP)  "Of predicted positive, how many correct?"
    Recall = TP / (TP + FN)     "Of actual positive, how many found?"

    PR curve shows precision vs recall at various thresholds.
    More informative than ROC for imbalanced datasets.

Functions to implement:
    1. precision_recall_at_threshold(y_true, y_scores, threshold)
       -> (precision, recall)

    2. precision_recall_curve(y_true, y_scores)
       -> (precisions, recalls, thresholds)

    3. average_precision(precisions, recalls) -> float
       - AP = Σ (R_n - R_{n-1}) * P_n

Example:
    y_true = [0, 0, 1, 1, 1]
    y_scores = [0.1, 0.4, 0.35, 0.7, 0.8]

    precisions, recalls, _ = precision_recall_curve(y_true, y_scores)
    ap = average_precision(precisions, recalls)

Edge Cases:
    - No positive predictions (precision undefined)
    - No positive labels (recall undefined)
    - All same score

Complexity:
    Time: O(n log n) for sorting
    Space: O(n) for thresholds
"""

import numpy as np
from pathlib import Path


def precision_recall_at_threshold(
    y_true: np.ndarray,
    y_scores: np.ndarray,
    threshold: float
) -> tuple[float, float]:
    """Compute precision and recall at a threshold.

    Args:
        y_true: True binary labels
        y_scores: Predicted probabilities
        threshold: Classification threshold

    Returns:
        Tuple of (precision, recall)
    """
    # TODO - you fill in here.
    return 0.0, 0.0


def precision_recall_curve(
    y_true: np.ndarray,
    y_scores: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute precision-recall curve.

    Args:
        y_true: True binary labels
        y_scores: Predicted probabilities

    Returns:
        Tuple of (precisions, recalls, thresholds)
    """
    # TODO - you fill in here.
    return np.array([]), np.array([]), np.array([])


def average_precision(
    precisions: np.ndarray,
    recalls: np.ndarray
) -> float:
    """Compute average precision (area under PR curve).

    Args:
        precisions: Precision values
        recalls: Recall values

    Returns:
        Average precision score
    """
    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_scores):
        y_true = np.array(y_true)
        y_scores = np.array(y_scores)
        precisions, recalls, _ = precision_recall_curve(y_true, y_scores)
        return round(average_precision(precisions, recalls), 4)

    exit(run_tests('precision_recall_tests.json', test_wrapper))
