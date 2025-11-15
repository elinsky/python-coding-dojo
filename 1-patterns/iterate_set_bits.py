import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '3-problems'))

from test_framework import generic_test


def count_set_bits(x: int) -> int:
    """
    Pattern Practice: Iterate Through Set Bits Only

    Goal: Count how many bits are set (efficient version)

    When to use: When you only care about 1-bits, not 0-bits
    Problems that use it: Parity, count set bits, check power of 2
    Key insight: Skip over 0-bits entirely; O(number of set bits) not O(total bits)

    Pattern to implement:
        count = 0
        while x:
            count += 1
            x &= (x - 1)  # Clear lowest set bit
        return count
    """
    # TODO - Implement the pattern here
    # count = 0
    # while x:
    #     count += 1
    #     x &= (x - 1)  # Clear lowest set bit
    # return count
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('iterate_set_bits.py',
                                       'iterate_set_bits.tsv',
                                       count_set_bits))
