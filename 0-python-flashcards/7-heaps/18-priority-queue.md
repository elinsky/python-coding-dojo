# Priority Queue with Heap

**Q:** How do I use a heap as a priority queue with (priority, item) pairs?

**A:** Push tuples with priority first

```python
heapq.heappush(h, (priority, item))
```
