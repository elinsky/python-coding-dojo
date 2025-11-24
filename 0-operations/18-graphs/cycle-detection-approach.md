# Cycle Detection in Directed Graph

**Q:** How do I detect a cycle in a directed graph using DFS?

**A:** Find a gray-to-gray edge (back edge to ancestor in DFS tree)

```python
# If we find an edge from gray vertex to gray vertex,
# there's a cycle
if current.color == GRAY and neighbor.color == GRAY:
    return True  # cycle found
```
