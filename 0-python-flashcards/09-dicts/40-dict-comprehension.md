# Dictionary Comprehension

**Q:** How do I create a dictionary using comprehension?

**A:** Use {key: value for ... } syntax

```python
# From two lists
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
d = {k: v for k, v in zip(keys, vals)}

# Transform existing dict
d2 = {k: v * 2 for k, v in d.items()}

# With condition
d3 = {k: v for k, v in d.items() if v > 1}
```
