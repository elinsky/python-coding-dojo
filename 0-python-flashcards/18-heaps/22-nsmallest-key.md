# N Smallest with Key

**Q:** Given a list of `(name, score)` tuples, how do you get the 3 tuples with the lowest scores using heapq?

**A:**

```python
heapq.nsmallest(3, items, key=lambda x: x[1])
```
