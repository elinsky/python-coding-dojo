from test_framework import generic_test


def parity(x: int) -> int:
    # variable to track parity. either 0 or 1.
    par = 0
    # could iterate over all the bits
    # faster would be iterate over 1s
    # forget how to do that tho
    while x:
        # isolate last bit
        last_bit = x & 1
        par = par ^ last_bit
        x = x >> 1
    return par


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
