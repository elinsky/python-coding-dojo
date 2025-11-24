# Edit Distance DP Pattern

**Q:** What's the recurrence pattern for edit distance / Levenshtein distance?

**A:** Consider three operations: insert, delete, substitute

```python
# dp[i][j] = min edits to transform A[0:i] to B[0:j]

if A[i-1] == B[j-1]:
    # Characters match, no edit needed
    dp[i][j] = dp[i-1][j-1]
else:
    # Take minimum of three operations
    dp[i][j] = 1 + min(
        dp[i-1][j-1],  # substitute A[i-1] with B[j-1]
        dp[i-1][j],    # delete A[i-1]
        dp[i][j-1]     # insert B[j-1]
    )
```

**Base cases:** dp[i][0] = i (delete all), dp[0][j] = j (insert all)
