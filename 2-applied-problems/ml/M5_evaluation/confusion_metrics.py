#!/usr/bin/env python3
"""M5.03: Confusion Matrix Metrics from Scratch

Implement confusion matrix and derived metrics.

Problem:
    Given predictions and true labels, compute:

    Confusion Matrix:
                    Predicted
                    Neg    Pos
    Actual  Neg     TN     FP
            Pos     FN     TP

    Metrics:
    - Accuracy = (TP + TN) / (TP + TN + FP + FN)
    - Precision = TP / (TP + FP)
    - Recall (Sensitivity) = TP / (TP + FN)
    - Specificity = TN / (TN + FP)
    - F1 = 2 * (Precision * Recall) / (Precision + Recall)

Functions to implement:
    1. confusion_matrix(y_true, y_pred) -> (tn, fp, fn, tp)

    2. accuracy(y_true, y_pred) -> float

    3. precision(y_true, y_pred) -> float

    4. recall(y_true, y_pred) -> float

    5. f1_score(y_true, y_pred) -> float

    6. all_metrics(y_true, y_pred) -> dict

Example:
    y_true = [0, 0, 1, 1, 1]
    y_pred = [0, 1, 1, 1, 0]

    # TN=1, FP=1, FN=1, TP=2
    # Accuracy = 3/5 = 0.6
    # Precision = 2/3 ≈ 0.667
    # Recall = 2/3 ≈ 0.667
    # F1 = 0.667

Edge Cases:
    - No positive predictions (precision = 0)
    - No positive labels (recall = 0)
    - All correct or all wrong

Complexity:
    Time: O(n)
    Space: O(1)
"""

import numpy as np
from pathlib import Path


def confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> tuple[int, int, int, int]:
    """Compute confusion matrix values.

    Args:
        y_true: True binary labels
        y_pred: Predicted binary labels

    Returns:
        Tuple of (TN, FP, FN, TP)
    """
    # TODO - you fill in here.
    return 0, 0, 0, 0


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute accuracy."""
    # TODO - you fill in here.
    return 0.0


def precision(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute precision (positive predictive value)."""
    # TODO - you fill in here.
    return 0.0


def recall(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute recall (sensitivity, true positive rate)."""
    # TODO - you fill in here.
    return 0.0


def f1_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute F1 score (harmonic mean of precision and recall)."""
    # TODO - you fill in here.
    return 0.0


def all_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Compute all classification metrics.

    Returns:
        Dict with accuracy, precision, recall, f1, and confusion matrix
    """
    # TODO - you fill in here.
    return {}


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        metrics = all_metrics(y_true, y_pred)
        return {k: round(v, 4) if isinstance(v, float) else v
                for k, v in metrics.items()}

    exit(run_tests('confusion_metrics_tests.json', test_wrapper))
