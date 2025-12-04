# Check if Fast Pointer Can Advance Two Steps

**Q:** How do I check if fast pointer can advance two steps? What is the time complexity?

**A:** Check fast and fast.next both exist. Time: O(1)

```python
if fast and fast.next:
    fast = fast.next.next
```
