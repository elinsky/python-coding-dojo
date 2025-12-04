# Longest Increasing Subsequence Pattern

**Q:** What's the DP pattern for longest increasing subsequence (LIS)?

**A:** dp[i] = length of longest increasing subseq ending at i

```python
# dp[i] = longest increasing subsequence ending at index i
dp = [1] * n  # base case: each element alone

for i in range(1, n):
    dp[i] = 1 + max(
        [dp[j] for j in range(i) if A[j] <= A[i]],
        default=0
    )

return max(dp)
```

**Key insight:** LIS ending at i extends some LIS ending at j < i where A[j] ≤ A[i]

Time: O(n²), Space: O(n)
