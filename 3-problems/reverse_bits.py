from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # i could loop here. 
    # get LSB. 
    result = 0
    for i in range(0, 64):
        lsb = (x >> i) & 1
        result = result << 1
        result = result | lsb
    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
