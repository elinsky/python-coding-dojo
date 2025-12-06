# Filter False

**Q:** How do I filter elements where predicate is False?

**A:** Use itertools.filterfalse()

```python
from itertools import filterfalse

list(filterfalse(lambda x: x % 2, range(10)))
# [0, 2, 4, 6, 8] - even numbers (where x%2 is False)

# Opposite of filter:
list(filter(lambda x: x % 2, range(10)))
# [1, 3, 5, 7, 9] - odd numbers
```
