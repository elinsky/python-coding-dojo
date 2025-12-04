# Create Frozenset

**Q:** How do I create an immutable set (hashable)? What is the time complexity?

**A:** Use frozenset() constructor. Time: O(n) where n is number of elements

```python
fs = frozenset([1, 2, 3])
fs = frozenset(s)  # Create from set
# Can be used as dict key or in another set
d[frozenset([1, 2])] = "value"
```
