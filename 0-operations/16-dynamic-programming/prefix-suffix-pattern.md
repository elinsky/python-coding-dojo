# Prefix/Suffix Subproblem Pattern

**Q:** What's the common pattern for DP on strings/arrays using prefixes?

**A:** Define state as "answer for first i elements"

```python
# dp[i] = answer for A[0:i] (first i elements)

# Last element is A[i-1]
# Base case: dp[0] = empty prefix

for i in range(1, n+1):
    # Consider A[i-1] (the i-th element)
    dp[i] = f(dp[i-1], A[i-1])
```
