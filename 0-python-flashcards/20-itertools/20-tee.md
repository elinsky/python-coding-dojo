# Tee (Duplicate Iterator)

**Q:** How do I create multiple independent iterators from one?

**A:** Use itertools.tee()

```python
from itertools import tee

data = iter([1, 2, 3, 4, 5])
it1, it2 = tee(data, 2)

list(it1)  # [1, 2, 3, 4, 5]
list(it2)  # [1, 2, 3, 4, 5]
```

Warning: Don't use original after tee(); significant memory if iterators diverge
