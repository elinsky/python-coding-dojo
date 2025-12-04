# Convert List to Max-Heap

**Q:** How do I convert a list to a max-heap in-place?

**A:** Negate all values then heapify

```python
h = [-x for x in lst]
heapq.heapify(h)
```
