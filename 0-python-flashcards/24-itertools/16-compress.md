# Compress

**Q:** How do I filter elements using a boolean selector?

**A:** Use itertools.compress()

```python
from itertools import compress

data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]
list(compress(data, selectors))
# ['a', 'c', 'e']

list(compress(range(10), [x % 2 for x in range(10)]))
# [1, 3, 5, 7, 9]
```
