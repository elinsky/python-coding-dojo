# Check Condition for All Vertices

**Q:** How do I check if all vertices in graph satisfy a condition?

**A:** Use all() with a generator expression

```python
return all(condition(v) for v in graph)
# or with function call
return all(dfs(v) for v in graph if not v.visited)
```
