# Create Frozenset

**Q:** How do I create an immutable set (hashable)?

**A:** Use frozenset() constructor

```python
fs = frozenset([1, 2, 3])
fs = frozenset(s)

# Can be used as dict key or in another set
d[frozenset([1, 2])] = "value"
```
