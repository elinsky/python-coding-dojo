"""Solution for M5.01: ROC Curve and AUC from Scratch"""
import numpy as np


def compute_tpr_fpr(
    y_true: np.ndarray,
    y_scores: np.ndarray,
    threshold: float
) -> tuple[float, float]:
    """Compute TPR and FPR at a given threshold."""
    y_pred = (y_scores >= threshold).astype(int)

    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    tn = np.sum((y_pred == 0) & (y_true == 0))
    fn = np.sum((y_pred == 0) & (y_true == 1))

    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    return tpr, fpr


def roc_curve(
    y_true: np.ndarray,
    y_scores: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute ROC curve."""
    # Get unique thresholds sorted in descending order
    thresholds = np.unique(y_scores)
    thresholds = np.sort(thresholds)[::-1]

    fprs = [0.0]
    tprs = [0.0]
    thresh_list = [thresholds[0] + 1]  # Start above max threshold

    for threshold in thresholds:
        tpr, fpr = compute_tpr_fpr(y_true, y_scores, threshold)
        fprs.append(fpr)
        tprs.append(tpr)
        thresh_list.append(threshold)

    # Add endpoint (1, 1)
    fprs.append(1.0)
    tprs.append(1.0)
    thresh_list.append(0.0)

    return np.array(fprs), np.array(tprs), np.array(thresh_list)


def auc(fprs: np.ndarray, tprs: np.ndarray) -> float:
    """Compute Area Under the ROC Curve using trapezoidal rule."""
    # Sort by FPR to ensure correct order
    sorted_indices = np.argsort(fprs)
    fprs = fprs[sorted_indices]
    tprs = tprs[sorted_indices]

    # Trapezoidal rule
    area = 0.0
    for i in range(1, len(fprs)):
        area += (fprs[i] - fprs[i-1]) * (tprs[i] + tprs[i-1]) / 2

    return area


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_scores):
        y_true = np.array(y_true)
        y_scores = np.array(y_scores)
        fprs, tprs, _ = roc_curve(y_true, y_scores)
        return round(auc(fprs, tprs), 4)

    exit(run_tests('roc_auc_tests.json', test_wrapper))
