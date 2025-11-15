def next_permutation(perm: list[int]) -> list[int]:
    """
    Pattern: Reverse Suffix to Sort

    Goal: Fix decreasing suffix by reversing it to get increasing order

    When to use: Permutation generation, lexicographic ordering
    Problems that use it: Next permutation, previous permutation
    Key insight: Decreasing suffix reversed = increasing suffix (sorted)
    """
    # Find longest decreasing suffix
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return []  # Last permutation

    # Find smallest element > perm[inversion_point] in suffix
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Reverse suffix to sort it
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm
