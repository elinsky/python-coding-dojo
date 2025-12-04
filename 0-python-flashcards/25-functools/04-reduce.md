# Reduce

**Q:** How do I reduce an iterable to a single value?

**A:** Use functools.reduce()

```python
from functools import reduce

# Sum
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 15

# Product
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 120

# With initial value
reduce(lambda x, y: x + y, [1, 2, 3], 10)
# 16
```
