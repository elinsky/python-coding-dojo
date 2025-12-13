# Why Not Remove from Visited on Backtrack?

**Q:** In DFS backtracking, we `path.pop()` when backtracking. Why don't we also remove from `visited`?

**A:** Once a cell leads to a dead end, there's no reason to revisit it from a different path - it will still be a dead end.

- `path`: represents the *current* path being explored (must backtrack)
- `visited`: represents *all* cells we've proven don't lead to the goal (keep them marked)
