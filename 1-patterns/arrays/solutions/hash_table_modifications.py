def random_subset(n: int, k: int) -> list[int]:
    """
    Pattern: Hash Table to Track Modifications

    Goal: Simulate large array with hash table tracking only changed entries

    When to use: Sparse modifications to large conceptual array
    Problems that use it: Random subset (k << n), sparse array operations
    Key insight: Track only A[i] where A[i] ≠ i; saves O(n) → O(k) space
    """
    import random

    changed_elements = {}
    for i in range(k):
        rand_idx = random.randrange(i, n)

        # Get actual values (using default if not in hash table)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)

        # Swap
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped

    return [changed_elements[i] for i in range(k)]
