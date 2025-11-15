import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def reverse_bits(x: int, num_bits: int = 64) -> int:
    """
    Template: Build Result Bit-by-Bit

    Problem: Given integer x and bit width num_bits, return x with its bits reversed

    Strategy: Build result from scratch by testing each bit position and setting its mirror position

    Patterns used:
    - Build Result Bit-by-Bit

    Memory hook: "Start at zero, OR to grow"

    Time complexity: O(n) where n = num_bits
    Space complexity: O(1)
    """
    # TODO - Implement the algorithm here
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('build_result_bit_by_bit.py',
                                       'build_result_bit_by_bit.tsv',
                                       reverse_bits))
