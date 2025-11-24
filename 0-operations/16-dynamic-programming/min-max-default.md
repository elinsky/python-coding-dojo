# Using max/min with default in DP

**Q:** How do you handle max/min over possibly empty list in DP?

**A:** Use default parameter in max/min for empty case

```python
# Problem: max of empty list raises ValueError

# WRONG: Will crash if no valid j
dp[i] = 1 + max([dp[j] for j in range(i) if condition])

# RIGHT: Provide default for empty case
dp[i] = 1 + max(
    [dp[j] for j in range(i) if condition],
    default=0
)

# Alternative: check first
values = [dp[j] for j in range(i) if condition]
dp[i] = 1 + max(values) if values else 0
```
