def can_reach_end(A: list[int]) -> bool:
    """
    Pattern: Track Furthest Reachable Position

    Goal: Maintain maximum position achievable while iterating

    When to use: Jump game, greedy reachability problems
    Problems that use it: Jump game, minimum jumps, array hopping
    Key insight: Track max reachable; fail if current position exceeds it
    """
    furthest_reach = 0
    last_index = len(A) - 1
    i = 0

    while i <= furthest_reach and furthest_reach < last_index:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1

    return furthest_reach >= last_index
