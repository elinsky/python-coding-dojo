import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def add(a: int, b: int) -> int:
    """
    Template: Ripple Carry

    Problem: Add two non-negative integers using only bitwise operations (no + operator)

    Strategy: Separate sum calculation from carry propagation; iterate until no carry remains

    Patterns used:
    - Ripple Carry

    Memory hook: "XOR for sum, AND for carry, shift carry LEFT"

    Time complexity: O(n) where n = number of bits
    Space complexity: O(1)
    """
    # TODO - Implement the algorithm here
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('ripple_carry.py',
                                       'ripple_carry.tsv',
                                       add))
