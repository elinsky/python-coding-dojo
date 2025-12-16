# Zip Longest

**Q:** How do I zip iterables of unequal length?

**A:** Use itertools.zip_longest() with fillvalue

```python
from itertools import zip_longest

list(zip_longest('ABC', [1, 2], fillvalue=None))
# [('A', 1), ('B', 2), ('C', None)]

list(zip_longest([1, 2, 3], [4, 5], fillvalue=0))
# [(1, 4), (2, 5), (3, 0)]
```
