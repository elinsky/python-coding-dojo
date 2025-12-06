# Space Optimization - Rolling Variables

**Q:** How do you optimize space when DP only depends on last few values?

**A:** Use rolling variables instead of full array

```python
# Instead of array:
# dp[i] = dp[i-1] + dp[i-2]

# Use rolling variables:
prev_2, prev_1 = 0, 1
for i in range(2, n):
    curr = prev_2 + prev_1
    prev_2, prev_1 = prev_1, curr
return prev_1
```
