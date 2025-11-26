# Tracking Visited Cells

**Q:** What are two ways to track visited cells in a maze, and when might you prefer each?

**A:**
1. **Separate set**: `visited = set()` - cleaner, doesn't mutate input
2. **In-place marking**: `maze[x][y] = BLACK` - saves space (no extra set)

Both are O(n*m) space asymptotically (path + recursion stack dominate), but in-place has smaller constant factor.
