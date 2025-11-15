def delete_duplicates(A: list[int]) -> int:
    """
    Pattern: Write Index / Slow-Fast Pointers

    Goal: Compact array by tracking separate read and write positions

    When to use: Removing elements in-place while maintaining order
    Problems that use it: Remove duplicates, remove value, filter elements
    Key insight: Write index trails read index; only write when condition met
    """
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):  # i is read index
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index
