# Check Any Neighbor Satisfies Condition

**Q:** How do I check if any neighbor satisfies a condition in graph traversal?

**A:** Use any() with a generator expression or map

```python
if any(condition(neighbor) for neighbor in graph[v]):
    # at least one neighbor satisfies condition

# or with map for function calls
if any(map(dfs_helper, vertex.edges)):
    return True
```
