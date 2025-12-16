# Chain from Iterable

**Q:** How do I flatten a nested iterable?

**A:** Use itertools.chain.from_iterable()

```python
from itertools import chain

nested = [[1, 2], [3, 4], [5, 6]]
list(chain.from_iterable(nested))
# [1, 2, 3, 4, 5, 6]

# vs chain() which needs unpacking:
list(chain(*nested))  # same result
```
