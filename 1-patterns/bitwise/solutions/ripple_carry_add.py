import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


def add(a: int, b: int) -> int:
    """
    Pattern: Ripple Carry Addition

    Goal: Add two numbers using only bitwise operations (no + operator)

    When to use: Implementing addition without + operator, as subroutine in multiply/other arithmetic
    Problems that use it: Problem 4.5 (Multiply calls add as subroutine)
    Key insight: Separate sum calculation from carry propagation; iterate until no carry
    """
    while b:
        sum_without_carry = a ^ b  # XOR gives sum ignoring carry
        carry = (a & b) << 1  # AND gives carry positions, shift left
        a = sum_without_carry
        b = carry
    return a


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('ripple_carry_add.py',
                                       'ripple_carry_add.tsv',
                                       add))
