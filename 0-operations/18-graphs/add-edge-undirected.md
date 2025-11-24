# Add Undirected Edge to Adjacency List

**Q:** How do I add an undirected edge between u and v in an adjacency list?

**A:** Add each vertex to the other's adjacency list

```python
graph[u].add(v)
graph[v].add(u)
```
