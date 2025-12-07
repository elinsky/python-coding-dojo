"""Solution for M2.03: Gradient Checker"""
import numpy as np
from typing import Callable


def numerical_gradient(f: Callable[[np.ndarray], float], x: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    """Compute numerical gradient using centered differences."""
    gradient = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += eps
        x_minus[i] -= eps
        gradient[i] = (f(x_plus) - f(x_minus)) / (2 * eps)
    return gradient


def gradient_check(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    eps: float = 1e-5,
    threshold: float = 1e-5
) -> tuple[bool, float]:
    """Check analytical gradient against numerical gradient."""
    grad_num = numerical_gradient(f, x, eps)
    grad_ana = grad_f(x)

    num_norm = np.linalg.norm(grad_num)
    ana_norm = np.linalg.norm(grad_ana)
    diff_norm = np.linalg.norm(grad_num - grad_ana)

    relative_error = diff_norm / (num_norm + ana_norm + 1e-10)
    passed = relative_error < threshold

    return passed, relative_error


if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(func_type, x):
        x = np.array(x, dtype=float)

        if func_type == 'quadratic':
            f = lambda x: np.sum(x**2)
            grad_f = lambda x: 2*x
        elif func_type == 'linear':
            f = lambda x: np.sum(x)
            grad_f = lambda x: np.ones_like(x)
        elif func_type == 'cubic':
            f = lambda x: np.sum(x**3)
            grad_f = lambda x: 3*x**2
        else:
            raise ValueError(f"Unknown func_type: {func_type}")

        passed, error = gradient_check(f, grad_f, x)
        return {'passed': passed, 'error': round(error, 10)}

    exit(run_tests('gradient_checker_tests.json', test_wrapper))
