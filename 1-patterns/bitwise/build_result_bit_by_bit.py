import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def reverse_bits(x: int, num_bits: int) -> int:
    """
    Pattern Practice: Build Result Bit-by-Bit

    Goal: Reverse the bits of x within num_bits width

    When to use: Constructing a new number based on bit positions
    Problems that use it: Reverse bits, swap bits, rearrange bits
    Key insight: Start with result=0, selectively set bits based on conditions
    """
    # TODO - Implement the pattern here
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('build_result_bit_by_bit.py',
                                       'build_result_bit_by_bit.tsv',
                                       reverse_bits))
