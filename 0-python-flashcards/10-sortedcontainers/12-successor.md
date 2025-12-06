# Find Successor in BST

**Q:** How do I find the successor (next larger value) in a BST in Python?

**A:** Use bisect_right

```python
idx = bst.bisect_right(k)  # Index of first value > k
successor = bst[idx] if idx < len(bst) else None
```
