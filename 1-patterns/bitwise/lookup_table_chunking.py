import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def reverse_bits_lookup(x: int) -> int:
    """
    Pattern Practice: Lookup Table with Chunking

    Goal: Reverse bits of a 64-bit number using precomputed 16-bit lookup table

    When to use: Operation done many times (amortize precomputation), operation is associative
    Problems that use it: Problem 4.1 (Parity with chunks), Problem 4.3 (Reverse bits with chunks)
    Key insight: Trade space for time; O(n/L) instead of O(n) per operation
    """
    # TODO - Implement the pattern here
    # Hint: Build lookup table for 16-bit reversal, then process 64-bit input in 4 chunks
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lookup_table_chunking.py',
                                       'lookup_table_chunking.tsv',
                                       reverse_bits_lookup))
