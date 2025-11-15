# Check if Fast Pointer Can Advance Two Steps

**Q:** How do I check if fast pointer can advance two steps?

**A:** Check fast and fast.next both exist

```python
if fast and fast.next:
    fast = fast.next.next
```
