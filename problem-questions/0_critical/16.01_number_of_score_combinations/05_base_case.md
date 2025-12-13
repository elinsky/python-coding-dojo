# Base Case

**Q:** What is the base case for the score combinations problem?

**A:** Score 0 always has exactly 1 way: use nothing.

```
dp[any_row][0] = 1
```

This is true for every row - there's always exactly one way to make score 0 regardless of which plays are available.
