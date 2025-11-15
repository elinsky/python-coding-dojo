def online_random_sample(stream, k: int) -> list:
    """
    Pattern: Reservoir Sampling / Online Selection

    Goal: Maintain uniform random sample from stream of unknown length

    When to use: Streaming data, unknown input size, memory constraints
    Problems that use it: Online sampling, random selection from stream
    Key insight: nth element included with probability k/n; replace random existing
    """
    import random
    import itertools

    # Keep first k elements
    sampling_results = list(itertools.islice(stream, k))
    num_seen_so_far = k

    for x in stream:
        num_seen_so_far += 1
        # Include with probability k/num_seen_so_far
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x

    return sampling_results
