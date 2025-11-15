import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def count_bits(x: int) -> int:
    """
    Template: Count Set Bits

    Problem: Given integer x, return the number of 1-bits in its binary representation

    Strategy: Iterate through only the set bits, clearing the lowest one each time

    Patterns used:
    - Iterate Through Set Bits Only

    Memory hook: "Each iteration removes exactly one bit"

    Time complexity: O(k) where k = number of set bits
    Space complexity: O(1)
    """
    # TODO - Implement the algorithm here
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_set_bits.py',
                                       'count_set_bits.tsv',
                                       count_bits))
