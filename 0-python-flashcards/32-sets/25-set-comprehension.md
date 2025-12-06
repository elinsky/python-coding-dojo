# Set Comprehension

**Q:** How do I create a set using comprehension?

**A:** Use {expression for ... } syntax

```python
s = {x * 2 for x in range(5)}  # {0, 2, 4, 6, 8}
s = {x for x in items if x > 0}  # With condition
s = {word.lower() for word in words}  # Transform
```
