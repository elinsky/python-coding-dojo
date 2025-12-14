# OrderedDict vs List of Tuples

**Q:** What's the difference between OrderedDict and a list of tuples?

**A:** OrderedDict has O(1) key lookup; list of tuples has O(1) index access

```python
# OrderedDict: fast key lookup, no index access
d = OrderedDict([('a', 1), ('b', 2)])
d['a']  # O(1)
d[0]    # KeyError

# List of tuples: fast index access, slow key lookup
lst = [('a', 1), ('b', 2)]
lst[0]  # O(1)
# Finding by key requires O(n) search
```
