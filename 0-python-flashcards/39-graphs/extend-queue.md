# Extend Queue with Multiple Items

**Q:** How do I add multiple items to a BFS queue at once?

**A:** Use extend() with a list or generator

```python
q.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
```
