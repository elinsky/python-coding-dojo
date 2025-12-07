#!/usr/bin/env python3
"""M2.03: Numerical Gradient Checker

Implement numerical gradient checking using finite differences.

Problem:
    Verify analytical gradients using numerical approximation:

    df/dx ≈ [f(x + ε) - f(x - ε)] / (2ε)

    This is the centered difference formula, more accurate than
    forward difference: [f(x + ε) - f(x)] / ε

    Compare numerical gradient to analytical gradient using:
    relative_error = ||grad_num - grad_ana|| / (||grad_num|| + ||grad_ana|| + ε)

Functions to implement:
    1. numerical_gradient(f, x, eps=1e-5) -> gradient
       - Compute numerical gradient using centered differences
       - Works for vector input x

    2. gradient_check(f, grad_f, x, eps=1e-5, threshold=1e-5) -> (passed, error)
       - Compare analytical grad_f(x) to numerical gradient
       - Return whether relative error is below threshold

Example:
    def f(x):  # x^2
        return x[0]**2

    def grad_f(x):  # 2x
        return np.array([2*x[0]])

    passed, error = gradient_check(f, grad_f, np.array([3.0]))
    # passed=True, error≈0

Edge Cases:
    - Gradient at x=0
    - Very small or large gradients
    - Non-smooth functions (will fail)

Complexity:
    Time: O(d) function evaluations for d-dimensional input
    Space: O(d) for gradient vector
"""

import numpy as np
from pathlib import Path
from typing import Callable


def numerical_gradient(
    f: Callable[[np.ndarray], float],
    x: np.ndarray,
    eps: float = 1e-5
) -> np.ndarray:
    """Compute numerical gradient using centered differences.

    Args:
        f: Scalar function to differentiate
        x: Point at which to compute gradient
        eps: Epsilon for finite difference

    Returns:
        Numerical gradient, same shape as x
    """
    # TODO - you fill in here.
    return np.array([])


def gradient_check(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    eps: float = 1e-5,
    threshold: float = 1e-5
) -> tuple[bool, float]:
    """Check analytical gradient against numerical gradient.

    Args:
        f: Scalar function
        grad_f: Analytical gradient function
        x: Point to check
        eps: Epsilon for numerical gradient
        threshold: Maximum allowed relative error

    Returns:
        Tuple of (passed, relative_error)
    """
    # TODO - you fill in here.
    return False, 1.0


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(func_type, x):
        x = np.array(x, dtype=float)

        if func_type == 'quadratic':
            # f(x) = x^2
            f = lambda x: np.sum(x**2)
            grad_f = lambda x: 2*x
        elif func_type == 'linear':
            # f(x) = sum(x)
            f = lambda x: np.sum(x)
            grad_f = lambda x: np.ones_like(x)
        elif func_type == 'cubic':
            # f(x) = sum(x^3)
            f = lambda x: np.sum(x**3)
            grad_f = lambda x: 3*x**2
        else:
            raise ValueError(f"Unknown func_type: {func_type}")

        passed, error = gradient_check(f, grad_f, x)
        return {'passed': passed, 'error': round(error, 10)}

    exit(run_tests('gradient_checker_tests.json', test_wrapper))
