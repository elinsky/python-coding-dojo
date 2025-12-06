# Sort Dictionary by Value

**Q:** How do I sort a dictionary by its values?

**A:** Use sorted() with key on items()

```python
d = {'a': 3, 'b': 1, 'c': 2}

# Sort by value
sorted_items = sorted(d.items(), key=lambda x: x[1])
# [('b', 1), ('c', 2), ('a', 3)]

# Or use itemgetter
from operator import itemgetter
sorted(d.items(), key=itemgetter(1))
```
