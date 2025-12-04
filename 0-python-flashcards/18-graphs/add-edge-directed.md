# Add Directed Edge to Adjacency List

**Q:** How do I add a directed edge from u to v in an adjacency list?

**A:** Add v to the set/list of u's neighbors

```python
graph[u].add(v)
# or for list
graph[u].append(v)
```
