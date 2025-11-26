# Edge Cases

**Q:** What edge cases must you handle when filling in the DP table?

**A:**
1. **First row (i == 0):** No row above exists, so "don't use this play" case = 0
2. **Score less than play value (j < plays[i]):** Can't use this play, so "use this play" case = 0

```python
case1 = dp[i-1][j] if i > 0 else 0
case2 = dp[i][j - plays[i]] if j >= plays[i] else 0
```
