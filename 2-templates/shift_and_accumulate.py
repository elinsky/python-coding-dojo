import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    Template: Shift-and-Conditional-Accumulate

    Problem: Given base x and exponent y, return x^y

    Strategy: Process each bit of exponent; if bit is 1, multiply result by current power;
              square the current power each iteration

    Patterns used:
    - Shift-and-Conditional-Accumulate

    Memory hook: "Selector shrinks right, value grows by squaring"

    Time complexity: O(log y)
    Space complexity: O(1)
    """
    # TODO - Implement the algorithm here
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('shift_and_accumulate.py',
                                       'shift_and_accumulate.tsv',
                                       power))
