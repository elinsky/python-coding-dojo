# Count (Infinite)

**Q:** How do I create an infinite counter?

**A:** Use itertools.count()

```python
from itertools import count, islice

# Infinite sequence starting at 10
counter = count(10)
list(islice(counter, 5))  # [10, 11, 12, 13, 14]

# With step
counter = count(0, 0.5)
list(islice(counter, 4))  # [0, 0.5, 1.0, 1.5]
```
