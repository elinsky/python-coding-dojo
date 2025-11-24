# Iterate Through Vertex Neighbors

**Q:** How do I iterate through all neighbors/edges of a vertex?

**A:** Loop through the vertex's edges list or adjacency list

```python
for neighbor in vertex.edges:
    # process neighbor
# or with adjacency list
for neighbor in graph[v]:
    # process neighbor
```
