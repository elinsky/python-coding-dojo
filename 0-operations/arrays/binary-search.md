# Binary Search on Sorted Array

**Q:** How do I perform binary search on sorted array?

**A:** Use bisect module

```python
import bisect
bisect.bisect(A, x)        # insertion point
bisect.bisect_left(A, x)   # leftmost
bisect.bisect_right(A, x)  # rightmost
```
