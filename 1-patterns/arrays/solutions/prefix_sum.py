def nonuniform_random_generation(values: list[int], probabilities: list[float]) -> int:
    """
    Pattern: Prefix Sum for Range Queries

    Goal: Convert point queries to interval membership via cumulative sums

    When to use: Weighted sampling, range sum queries, interval search
    Problems that use it: Random with probabilities, range sums, sliding window
    Key insight: Binary search on prefix sums converts probability to interval
    """
    import random
    import bisect

    # Build prefix sum array
    prefix_sum_of_probabilities = []
    cumsum = 0
    for p in probabilities:
        cumsum += p
        prefix_sum_of_probabilities.append(cumsum)

    # Map uniform random to interval
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]
