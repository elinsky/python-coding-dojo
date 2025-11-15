def generate_primes(n: int) -> list[int]:
    """
    Pattern: Boolean Array for Set Membership

    Goal: Use array index as implicit key; value tracks membership/state

    When to use: When domain is small integers; need O(1) lookup
    Problems that use it: Sieve of Eratosthenes, count occurrences, seen set
    Key insight: Array position = element value; avoids hash table overhead
    """
    if n < 2:
        return []

    # is_prime[i] represents if i is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # Sieve out multiples
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return primes
