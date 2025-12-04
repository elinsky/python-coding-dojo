# Common Reduce Patterns

**Q:** What are common reduce patterns?

**A:** Aggregation operations:

```python
from functools import reduce
import operator

nums = [1, 2, 3, 4, 5]

# Sum (prefer sum() builtin)
reduce(operator.add, nums)  # 15

# Product
reduce(operator.mul, nums)  # 120

# Max (prefer max() builtin)
reduce(lambda a, b: a if a > b else b, nums)

# Flatten lists
lists = [[1, 2], [3, 4], [5]]
reduce(operator.add, lists)  # [1, 2, 3, 4, 5]
```
