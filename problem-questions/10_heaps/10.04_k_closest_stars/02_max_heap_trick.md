# Max-Heap Trick

**Q:** How do you simulate a max-heap in Python using `heapq`?

**A:** Negate the values when pushing: `heappush(heap, (-value, item))`
