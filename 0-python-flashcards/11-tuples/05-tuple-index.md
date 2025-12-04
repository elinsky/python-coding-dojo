# Find Index in Tuple

**Q:** How do I find the first index of a value in a tuple?

**A:** Use index() method (raises ValueError if not found)

```python
t = (1, 2, 3, 4, 5)
idx = t.index(3)  # 2
idx = t.index(3, 1, 4)  # Search in slice [1:4]
```
