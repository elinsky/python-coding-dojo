# Sum Recurrence Pattern (Counting)

**Q:** What's the pattern for DP recurrences that count ways/combinations?

**A:** Sum the counts from all ways to reach current state

```python
# Counting pattern (e.g., number of ways)
dp[i] = sum(dp[i-k] for k in choices)

# Or explicitly
dp[i] = dp[i-k1] + dp[i-k2] + dp[i-k3]

# Example: climbing stairs
ways[n] = ways[n-1] + ways[n-2]
```
