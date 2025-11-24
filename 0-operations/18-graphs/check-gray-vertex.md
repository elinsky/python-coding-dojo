# Check if Vertex is Gray (Processing)

**Q:** How do I check if a vertex is currently being processed (gray) in DFS?

**A:** Check if vertex color equals GRAY

```python
if vertex.color == GraphVertex.gray:
    # currently processing (cycle detected!)
```
