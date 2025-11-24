# Knapsack DP Pattern

**Q:** What's the state definition pattern for knapsack-type problems?

**A:** dp[i][w] = best using first i items with capacity w

```python
# dp[i][w] = optimal value using items[0:i] with capacity w
dp = [[0] * (W+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(W+1):
        # Don't take item i-1
        without = dp[i-1][w]

        # Take item i-1 (if fits)
        with_item = 0
        if w >= weight[i-1]:
            with_item = value[i-1] + dp[i-1][w-weight[i-1]]

        dp[i][w] = max(without, with_item)
```
