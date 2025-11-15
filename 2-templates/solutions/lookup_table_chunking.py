import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


# Precompute bit reversal for all 16-bit numbers (done once at module load)
def _precompute_reverse():
    """Helper to reverse bits in a 16-bit number"""
    def reverse_16_bits(val):
        result = 0
        for i in range(16):
            if val & (1 << i):
                result |= (1 << (15 - i))
        return result

    return [reverse_16_bits(i) for i in range(1 << 16)]


PRECOMPUTED_REVERSE = _precompute_reverse()


def reverse_bits(x: int) -> int:
    """
    Template: Lookup Table Chunking

    Problem: Reverse the bits of a 64-bit integer using precomputed lookup table

    Strategy: Precompute bit reversal for all 16-bit values; split 64-bit input into four 16-bit chunks;
              reverse each chunk via lookup, then combine in reversed order

    Patterns used:
    - Lookup Table Chunking

    Memory hook: "Precompute small, chunk large, combine results"

    Time complexity: O(n/L) where n = word size, L = chunk size (effectively O(1) after precomputation)
    Space complexity: O(2^L) for lookup table
    """
    MASK = 0xFFFF
    CHUNK_SIZE = 16

    # Process 4 chunks of 16 bits each, reverse their order
    return (
        PRECOMPUTED_REVERSE[x & MASK] << (3 * CHUNK_SIZE) |
        PRECOMPUTED_REVERSE[(x >> CHUNK_SIZE) & MASK] << (2 * CHUNK_SIZE) |
        PRECOMPUTED_REVERSE[(x >> (2 * CHUNK_SIZE)) & MASK] << CHUNK_SIZE |
        PRECOMPUTED_REVERSE[(x >> (3 * CHUNK_SIZE)) & MASK]
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lookup_table_chunking.py',
                                       'lookup_table_chunking.tsv',
                                       reverse_bits))
