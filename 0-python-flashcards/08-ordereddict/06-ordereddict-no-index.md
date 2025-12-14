# OrderedDict No Index Access

**Q:** Can you access OrderedDict items by index/position?

**A:** No direct index access. Use `popitem(last=True/False)` for ends, or convert to list for arbitrary positions.

```python
d[0]  # KeyError - no key called 0
d.popitem(last=False)  # Remove and return first
d.popitem(last=True)   # Remove and return last
list(d.items())[idx]   # O(n) access by position
```
