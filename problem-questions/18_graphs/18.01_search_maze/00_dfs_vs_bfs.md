# DFS vs BFS for Maze Problems

**Q:** When should you use DFS vs BFS for maze/graph path-finding?

**A:**
- **DFS**: When you need *any* valid path. The recursion stack naturally builds the path.
- **BFS**: When you need the *shortest* path. Requires extra bookkeeping to reconstruct the path.

For "find a path" problems, DFS is simpler to implement.
