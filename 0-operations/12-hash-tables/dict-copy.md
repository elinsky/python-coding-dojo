# Shallow Copy Dictionary

**Q:** How do I create a shallow copy of a dictionary? What is the time complexity?

**A:** Use copy() method or dict() constructor. Time: O(n)

```python
d2 = d1.copy()
d2 = dict(d1)
```
