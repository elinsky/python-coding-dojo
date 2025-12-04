# Max/Min Recurrence Pattern

**Q:** What's the pattern for DP recurrences that maximize/minimize over choices?

**A:** Use max()/min() over all possible decisions

```python
# Maximization (e.g., max profit, max value)
dp[i] = max(
    choice1 + dp[i-k1],
    choice2 + dp[i-k2],
    # ... more choices
)

# Minimization (e.g., min cost, min edits)
dp[i] = min(
    cost1 + dp[i-k1],
    cost2 + dp[i-k2],
    # ... more choices
)
```
