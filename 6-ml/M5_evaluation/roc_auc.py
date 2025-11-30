#!/usr/bin/env python3
"""M5.01: ROC Curve and AUC from Scratch

Implement ROC curve computation and AUC calculation.

Problem:
    ROC (Receiver Operating Characteristic) curve plots:
    - True Positive Rate (TPR) = TP / (TP + FN) = Recall
    - False Positive Rate (FPR) = FP / (FP + TN)

    At various classification thresholds.

    AUC = Area Under the ROC Curve (use trapezoidal rule)

Functions to implement:
    1. compute_tpr_fpr(y_true, y_scores, threshold) -> (tpr, fpr)

    2. roc_curve(y_true, y_scores) -> (fprs, tprs, thresholds)
       - Return FPR, TPR at each unique threshold
       - Include (0,0) and (1,1) endpoints

    3. auc(fprs, tprs) -> float
       - Area under curve using trapezoidal rule

Example:
    y_true = [0, 0, 1, 1]
    y_scores = [0.1, 0.4, 0.35, 0.8]

    fprs, tprs, thresholds = roc_curve(y_true, y_scores)
    area = auc(fprs, tprs)
    # area = 0.75

Edge Cases:
    - All same class
    - Perfect predictions (AUC = 1.0)
    - Random predictions (AUC ≈ 0.5)
    - Tied scores

Complexity:
    Time: O(n log n) for sorting by scores
    Space: O(n) for thresholds
"""

import numpy as np
from pathlib import Path


def compute_tpr_fpr(
    y_true: np.ndarray,
    y_scores: np.ndarray,
    threshold: float
) -> tuple[float, float]:
    """Compute TPR and FPR at a given threshold.

    Args:
        y_true: True binary labels
        y_scores: Predicted probabilities
        threshold: Classification threshold

    Returns:
        Tuple of (TPR, FPR)
    """
    # TODO - you fill in here.
    return 0.0, 0.0


def roc_curve(
    y_true: np.ndarray,
    y_scores: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute ROC curve.

    Args:
        y_true: True binary labels
        y_scores: Predicted probabilities

    Returns:
        Tuple of (FPRs, TPRs, thresholds)
    """
    # TODO - you fill in here.
    return np.array([]), np.array([]), np.array([])


def auc(fprs: np.ndarray, tprs: np.ndarray) -> float:
    """Compute Area Under the ROC Curve.

    Args:
        fprs: False positive rates
        tprs: True positive rates

    Returns:
        AUC value
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
        fprs, tprs, _ = roc_curve(y_true, y_scores)
        return round(auc(fprs, tprs), 4)

    exit(run_tests('roc_auc_tests.json', test_wrapper))
