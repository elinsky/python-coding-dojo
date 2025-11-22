# Slice Array

**Q:** How do I slice from index i (inclusive) to j (exclusive)?

**A:** Use slice notation A[i:j] - O(k) time where k = j-i

```python
A[i:j]    # elements from i to j-1 (i inclusive, j exclusive)
A[i:]     # from i to end
A[:j]     # from start to j-1
A[i:j:k]  # from i to j-1 with step k
```
