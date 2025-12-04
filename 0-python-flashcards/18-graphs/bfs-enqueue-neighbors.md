# BFS Enqueue Neighbors

**Q:** How do I enqueue all neighbors of current vertex in BFS?

**A:** Append each neighbor to the deque

```python
for neighbor in graph[v]:
    if neighbor not in visited:
        q.append(neighbor)
```
