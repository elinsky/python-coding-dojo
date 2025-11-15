import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


def add(a: int, b: int) -> int:
    """Helper: Add using ripple carry (no + operator)."""
    while b:
        sum_without_carry = a ^ b
        carry = (a & b) << 1
        a = sum_without_carry
        b = carry
    return a


def multiply(x: int, y: int) -> int:
    """
    Pattern: Shift-and-Conditional-Accumulate

    Goal: Multiply two numbers using grade-school algorithm with bitwise operations

    When to use: Grade-school algorithms (multiply, power), processing each bit of a control value
    Problems that use it: Problem 4.5 (Multiply), Problem 4.7 (Power)
    Key insight: Processes selector bits right-to-left, builds result incrementally
    """
    result = 0
    while y:
        if y & 1:
            result = add(result, x)  # ADD if multiplier bit is 1
        x <<= 1  # Shift multiplicand left
        y >>= 1  # Shift multiplier right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('shift_and_accumulate.py',
                                       'shift_and_accumulate.tsv',
                                       multiply))
