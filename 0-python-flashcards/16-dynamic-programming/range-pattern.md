# Range/Interval DP Pattern

**Q:** What's the pattern for DP on ranges/intervals [i, j]?

**A:** Iterate by increasing interval length

```python
n = len(A)
dp = [[0] * n for _ in range(n)]

# Base case: length 1 intervals
for i in range(n):
    dp[i][i] = base_case

# Iterate by increasing length
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        # dp[i][j] depends on smaller intervals
        dp[i][j] = f(dp, i, j)
```
