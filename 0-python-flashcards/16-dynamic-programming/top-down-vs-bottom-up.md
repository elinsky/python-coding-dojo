# Top-Down vs Bottom-Up

**Q:** What's the difference between top-down and bottom-up DP?

**A:**

**Top-down (Memoization):**
- Recursive
- Cache is dict or array with -1 sentinel
- Only computes needed subproblems
- Easier to write for complex state

**Bottom-up (Tabulation):**
- Iterative
- Table filled systematically
- Computes all subproblems
- Often easier to optimize space
- Usually faster (no recursion overhead)

```python
# Top-down
def dp(n, cache={}):
    if n <= 1: return n
    if n not in cache:
        cache[n] = dp(n-1) + dp(n-2)
    return cache[n]

# Bottom-up
def dp(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
