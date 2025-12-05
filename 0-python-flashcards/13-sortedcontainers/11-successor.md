# Find Successor in BST

**Q:** How do I find the successor (next larger value) in a BST in Python?

**A:** Use bisect_right

```python
idx = s.bisect_right(k)  # Index of first value > k
successor = s[idx] if idx < len(s) else None
```
