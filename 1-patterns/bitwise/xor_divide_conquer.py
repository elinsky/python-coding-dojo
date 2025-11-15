import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def compute_parity(x: int) -> int:
    """
    Pattern Practice: XOR Divide-and-Conquer (Associativity)

    Goal: Compute parity (0 if even number of 1s, 1 if odd) in O(log n) time

    When to use: Parity calculation, any associative/commutative operation on bits
    Problems that use it: Problem 4.1 (Parity - optimal O(log n) solution)
    Key insight: Each XOR "folds" half the bits into the other half; works because XOR is associative
    """
    # TODO - Implement the pattern here
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('xor_divide_conquer.py',
                                       'xor_divide_conquer.tsv',
                                       compute_parity))
