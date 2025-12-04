# Identifying State Variables

**Q:** How do you identify what should be the state (parameters) in DP?

**A:** Ask: "What info do I need to solve any subproblem?"

**Common state patterns:**
- **Single index**: dp[i] = answer for prefix/first i elements
- **Two indices**: dp[i][j] = answer for range [i,j] or two strings
- **Index + capacity**: dp[i][w] = answer for first i items with capacity w
- **Index + count**: dp[i][k] = answer for first i elements with k items used
- **Position + state**: dp[i][s] = answer at position i in state s

**Example:** Knapsack
- Need: which items considered + remaining capacity
- State: dp[i][w] = best value using items 0..i-1 with capacity w
