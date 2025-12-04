from test_framework import generic_test


def square_root(k: int) -> int:
    # basically square root and floor it
    # search space is [0, sqrt(k)]
    # could build and array of all values. then do a binary search
    # can i do it with less memory though?
    if k in {0, 1}:
        return k
    # invariant - search space inclusive of left and right
    left = 0
    right = k
    # I want the largest value where val * val <= k
    while left < right:  # TODO - double check < or <=
        mid = ((right - left) // 2) + left # TODO double check for edge cases
        # is mid a valid solution?
        is_valid = True if mid * mid <= k else False
        if not is_valid:
            right = mid - 1
        else:  # is valid
            left = mid
        if right - 1 == left:
            break
    
    is_left_valid = True if left * left <= k else False
    is_right_valid = True if right * right <= k else False

    if is_right_valid:
        return right
    else:
        return left




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
