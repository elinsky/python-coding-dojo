# Create Set

**Q:** How do I create a set?

**A:** Use curly braces or set() constructor

```python
s = set()  # Empty set (not {} which is dict)
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}
s = {x for x in range(10) if x % 2 == 0}
```
