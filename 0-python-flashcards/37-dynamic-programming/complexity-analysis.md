# DP Complexity Analysis

**Q:** How do you analyze time/space complexity of DP solutions?

**A:**

**Time complexity:**
- Number of states × Time per state
- States = possible values of parameters
- Example: dp[i][j] with i∈[0,n], j∈[0,m] → O(nm) states
- If each state takes O(k) to compute → O(nmk) total

**Space complexity:**
- Size of cache/table
- Can often reduce by recycling (e.g., O(n²) → O(n))

```python
# O(n²) time: n states, each takes O(n) time
for i in range(n):
    dp[i] = max(dp[j] for j in range(i))

# O(nm) space for 2D table
dp = [[0] * m for _ in range(n)]
```
