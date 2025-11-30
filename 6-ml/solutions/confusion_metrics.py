"""Solution for M5.03: Confusion Matrix Metrics from Scratch"""
import numpy as np


def confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> tuple[int, int, int, int]:
    """Compute confusion matrix values."""
    tp = int(np.sum((y_pred == 1) & (y_true == 1)))
    fp = int(np.sum((y_pred == 1) & (y_true == 0)))
    tn = int(np.sum((y_pred == 0) & (y_true == 0)))
    fn = int(np.sum((y_pred == 0) & (y_true == 1)))
    return tn, fp, fn, tp


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute accuracy."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred)
    return (tp + tn) / (tp + tn + fp + fn)


def precision(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute precision (positive predictive value)."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred)
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0


def recall(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute recall (sensitivity, true positive rate)."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred)
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0


def f1_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute F1 score (harmonic mean of precision and recall)."""
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def all_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Compute all classification metrics."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred)
    return {
        'accuracy': accuracy(y_true, y_pred),
        'precision': precision(y_true, y_pred),
        'recall': recall(y_true, y_pred),
        'f1': f1_score(y_true, y_pred),
        'tn': tn,
        'fp': fp,
        'fn': fn,
        'tp': tp
    }


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        metrics = all_metrics(y_true, y_pred)
        return {k: round(v, 4) if isinstance(v, float) else v
                for k, v in metrics.items()}

    exit(run_tests('confusion_metrics_tests.json', test_wrapper))
