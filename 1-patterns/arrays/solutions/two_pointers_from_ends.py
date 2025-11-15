def partition_even_odd(A: list[int]) -> None:
    """
    Pattern: Two Pointers from Ends

    Goal: Partition array by moving elements from both ends toward center

    When to use: When you need to rearrange elements into two groups
    Problems that use it: Even/odd partition, Dutch flag, two-sum in sorted array
    Key insight: Process from both ends simultaneously; O(n) time, O(1) space
    """
    left, right = 0, len(A) - 1
    while left < right:
        if A[left] % 2 == 0:
            left += 1
        else:
            A[left], A[right] = A[right], A[left]
            right -= 1
