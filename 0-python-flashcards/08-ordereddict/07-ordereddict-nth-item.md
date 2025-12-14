# Get Nth Item from OrderedDict

**Q:** How do you get the nth item from an OrderedDict?

**A:** Convert to list first (O(n) operation)

```python
list(d.items())[n]   # (key, value) tuple at position n
list(d.keys())[n]    # key at position n
list(d.values())[n]  # value at position n
```
