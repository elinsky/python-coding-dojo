def plus_one(A: list[int]) -> list[int]:
    """
    Pattern: Process from Back to Avoid Shifts

    Goal: Handle carry/overflow by processing least significant digit first

    When to use: Arbitrary precision arithmetic, digit manipulation
    Problems that use it: Add one, add two numbers, multiply arrays
    Key insight: Start at back, propagate carry forward; only grow if needed
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
