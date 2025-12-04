# DFS Recursive Pattern

**Q:** What is the basic recursive DFS pattern?

**A:** Mark as visited, then recursively visit unvisited neighbors

```python
def dfs(v, visited):
    if v in visited:
        return
    visited.add(v)
    for neighbor in graph[v]:
        dfs(neighbor, visited)
```
