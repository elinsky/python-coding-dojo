# Grid Path DP Pattern

**Q:** What's the pattern for DP on grid paths (can only go right/down)?

**A:** dp[i][j] = answer at cell (i,j) from dp[i-1][j] and dp[i][j-1]

```python
m, n = len(grid), len(grid[0])
dp = [[0] * n for _ in range(m)]

# Base cases: first row and column
dp[0][0] = grid[0][0]
for i in range(1, m):
    dp[i][0] = dp[i-1][0] + grid[i][0]
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# Fill table
for i in range(1, m):
    for j in range(1, n):
        # Can only come from top or left
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], grid[i][j])
```
