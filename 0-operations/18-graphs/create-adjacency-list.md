# Create Adjacency List with Defaultdict

**Q:** How do I create an adjacency list representation of a graph using defaultdict?

**A:** Use collections.defaultdict(set) or defaultdict(list) for the graph

```python
graph = collections.defaultdict(set)
# or
graph = collections.defaultdict(list)
```
