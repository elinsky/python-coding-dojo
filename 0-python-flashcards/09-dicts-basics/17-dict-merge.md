# Merge Dictionaries

**Q:** How do I merge dictionaries (Python 3.9+)?

**A:** Use | (merge) or |= (update) operators

```python
d3 = d1 | d2  # d2 values override d1
d1 |= d2  # Equivalent to d1.update(d2)
```
