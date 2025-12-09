# Create Max-Heap from List

**Q:** How do you create a max-heap from a list of values?

**A:** Negate all values then heapify

```python
h = [-x for x in lst]
heapq.heapify(h)
```
