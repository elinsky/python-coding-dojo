# Cartesian Product

**Q:** How do I get the Cartesian product of iterables?

**A:** Use itertools.product()

```python
from itertools import product

list(product('AB', [1, 2]))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# Equivalent to nested loops
list(product(range(2), repeat=3))
# [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
```
