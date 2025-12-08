from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string


def int_to_string(x: int) -> str:
    # ok waht am i going to do here?
    # left to right or right ot left?
    # can probably strip off last digit.
    # convert to string
    # shift x right
    # String. so join at end
    int_to_string_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    if x == 0:
        return '0'
    is_negative = True if x < 0 else False
    if is_negative:
        x = abs(x)
    result = []
    while x > 0:
        # strip last digit
        last_digit_int = x % 10
        # chop off last digit
        x = x // 10
        last_digit_str = int_to_string_map[last_digit_int]
        result.append(last_digit_str)
    if is_negative:
        result.append('-') # TODO - double check do this at start not end:
    # else:
        # result.append('+')

    return ''.join(result[::-1])


def string_to_int(s: str) -> int:
    string_to_int_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # can't use the int() built-in function
    # ok am i iterating left ot right or right to left?
    if s == '0':
        return 0
    is_negative = True if s[0] == '-' else False
    result = 0
    for digit_str in s:
        if digit_str == '-':
            continue
        if digit_str == '+':
            continue
        result = result * 10
        digit_int = string_to_int_map[digit_str]
        result = result + digit_int

    # TODO - you fill in here.
    if is_negative:
        result = result * -1
    return result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
