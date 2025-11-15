import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


def has_alternating_bits(x: int) -> bool:
    """
    Pattern: Process Bits Right-to-Left (All Bits)

    Goal: Check if x has alternating bits (0101... or 1010...)

    When to use: When you need to examine every bit in sequence
    Problems that use it: Alternating bits check, convert to different base
    Key insight: Extract bit, process it, shift right, repeat
    """
    if x == 0:
        return True

    prev_bit = x & 1
    x >>= 1
    while x:
        curr_bit = x & 1
        if curr_bit == prev_bit:
            return False
        prev_bit = curr_bit
        x >>= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('process_bits_right_to_left.py',
                                       'process_bits_right_to_left.tsv',
                                       has_alternating_bits))
