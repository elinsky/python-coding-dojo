# Check if Graph is Bipartite

**Q:** How do I check if a graph is bipartite (2-colorable)?

**A:** Use BFS; check if any edge connects two vertices at same distance

```python
# Run BFS and assign levels
# If edge connects two vertices at same level,
# not bipartite
if neighbor.distance == current.distance:
    return False  # same level, not bipartite
```
