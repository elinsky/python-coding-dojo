# Use Slow and Fast Pointers

**Q:** How do I use slow and fast pointers (2x speed)? What is the time complexity?

**A:** Advance slow by 1, fast by 2. Time: O(1)

```python
slow, fast = slow.next, fast.next.next
```
