# Find Predecessor in BST

**Q:** How do I find the predecessor (next smaller value) in a BST in Python?

**A:** Use bisect_left

```python
idx = s.bisect_left(k)  # Index of first value >= k
predecessor = s[idx - 1] if idx > 0 else None
```
