# Merge with Key

**Q:** Given two sorted lists of `(timestamp, event)` tuples (sorted by timestamp), how do you merge them into a single sorted iterator?

**A:**

```python
heapq.merge(list1, list2, key=lambda x: x[0])
```
