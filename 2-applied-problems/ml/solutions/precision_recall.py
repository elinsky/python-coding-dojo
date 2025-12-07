"""Solution for M5.02: Precision-Recall Curve from Scratch"""
import numpy as np


def precision_recall_at_threshold(
    y_true: np.ndarray,
    y_scores: np.ndarray,
    threshold: float
) -> tuple[float, float]:
    """Compute precision and recall at a threshold."""
    y_pred = (y_scores >= threshold).astype(int)

    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    fn = np.sum((y_pred == 0) & (y_true == 1))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    return precision, recall


def precision_recall_curve(
    y_true: np.ndarray,
    y_scores: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute precision-recall curve."""
    # Get unique thresholds sorted in descending order
    thresholds = np.unique(y_scores)
    thresholds = np.sort(thresholds)[::-1]

    precisions = []
    recalls = []
    thresh_list = []

    for threshold in thresholds:
        prec, rec = precision_recall_at_threshold(y_true, y_scores, threshold)
        precisions.append(prec)
        recalls.append(rec)
        thresh_list.append(threshold)

    # Add endpoint (precision=positive rate at recall=1)
    precisions.append(np.sum(y_true) / len(y_true))
    recalls.append(1.0)
    thresh_list.append(0.0)

    return np.array(precisions), np.array(recalls), np.array(thresh_list)


def average_precision(
    precisions: np.ndarray,
    recalls: np.ndarray
) -> float:
    """Compute average precision (area under PR curve) using sklearn-style interpolation."""
    # Sort by recall descending to process from high to low recall
    sorted_indices = np.argsort(-recalls)
    recalls = recalls[sorted_indices]
    precisions = precisions[sorted_indices]

    # Compute interpolated precision (max precision at recall >= r)
    interp_precisions = np.maximum.accumulate(precisions)

    # Resort by recall ascending for area calculation
    sorted_indices = np.argsort(recalls)
    recalls = recalls[sorted_indices]
    interp_precisions = interp_precisions[sorted_indices[::-1]]  # reverse accumulation

    # AP = sum of (R_n - R_{n-1}) * P_interp_n
    ap = 0.0
    prev_recall = 0.0
    for i in range(len(recalls)):
        if recalls[i] > prev_recall:
            ap += (recalls[i] - prev_recall) * interp_precisions[i]
            prev_recall = recalls[i]

    return ap


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_scores):
        y_true = np.array(y_true)
        y_scores = np.array(y_scores)
        precisions, recalls, _ = precision_recall_curve(y_true, y_scores)
        return round(average_precision(precisions, recalls), 4)

    exit(run_tests('precision_recall_tests.json', test_wrapper))
