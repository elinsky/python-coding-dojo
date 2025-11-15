import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


# Precompute lookup table for 16-bit reversal
def reverse_16_bits(x: int) -> int:
    """Reverse bits in a 16-bit number."""
    result = 0
    for i in range(16):
        if x & (1 << i):
            result |= (1 << (15 - i))
    return result


# Build lookup table once (memoized at module level)
LOOKUP_TABLE = [reverse_16_bits(i) for i in range(2**16)]


def reverse_bits_lookup(x: int) -> int:
    """
    Pattern: Lookup Table with Chunking

    Goal: Reverse bits of a 64-bit number using precomputed 16-bit lookup table

    When to use: Operation done many times (amortize precomputation), operation is associative
    Problems that use it: Problem 4.1 (Parity with chunks), Problem 4.3 (Reverse bits with chunks)
    Key insight: Trade space for time; O(n/L) instead of O(n) per operation
    """
    MASK = 0xFFFF  # 16-bit mask
    CHUNK_SIZE = 16

    # Process 4 chunks of 16 bits each, reverse their order
    return (
        LOOKUP_TABLE[x & MASK] << (3 * CHUNK_SIZE) |
        LOOKUP_TABLE[(x >> CHUNK_SIZE) & MASK] << (2 * CHUNK_SIZE) |
        LOOKUP_TABLE[(x >> (2 * CHUNK_SIZE)) & MASK] << CHUNK_SIZE |
        LOOKUP_TABLE[(x >> (3 * CHUNK_SIZE)) & MASK]
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lookup_table_chunking.py',
                                       'lookup_table_chunking.tsv',
                                       reverse_bits_lookup))
