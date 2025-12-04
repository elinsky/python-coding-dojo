# Frozenset Operations

**Q:** What operations can frozensets perform?

**A:** All set operations except modifications

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])

fs1 | fs2  # Union
fs1 & fs2  # Intersection
fs1 - fs2  # Difference
1 in fs1   # Membership

# NO: add, remove, update, etc.
```
