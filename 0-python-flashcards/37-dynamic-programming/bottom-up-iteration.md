# Bottom-Up Iteration Pattern

**Q:** What's the typical pattern for bottom-up DP (iterative)?

**A:** Iterate from base cases up, filling table using recurrence

```python
# Initialize with base cases
dp[0] = base_case_0
dp[1] = base_case_1

# Iterate and fill using recurrence
for i in range(2, n):
    dp[i] = recurrence(dp, i)

return dp[n-1]
```
