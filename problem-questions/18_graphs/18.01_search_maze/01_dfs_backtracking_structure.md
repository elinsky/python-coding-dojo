# DFS Backtracking Structure

**Q:** What's the structure of a DFS backtracking function for path-finding?

**A:**
1. Mark current as visited and add to path
2. If at goal, return True
3. For each valid unvisited neighbor, recurse; if it returns True, return True
4. Pop from path (backtrack) and return False

Key: Add to path *before* checking goal, pop *after* all neighbors fail.
