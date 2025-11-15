def random_sampling(k: int, A: list[int]) -> None:
    """
    Pattern: Random Sampling with Swap-to-Front

    Goal: Build random subset by swapping selected elements to front

    When to use: Random subset selection, shuffling, sampling without replacement
    Problems that use it: Random sample, random permutation, reservoir sampling
    Key insight: Partition array into [selected | unselected]; shrink unselected region
    """
    import random
    for i in range(k):
        # Generate random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    # Result is A[:k]
