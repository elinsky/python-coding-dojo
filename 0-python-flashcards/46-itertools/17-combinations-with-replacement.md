# Combinations with Replacement

**Q:** How do I get combinations allowing repeated elements?

**A:** Use itertools.combinations_with_replacement()

```python
from itertools import combinations_with_replacement

list(combinations_with_replacement('AB', 2))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]

list(combinations_with_replacement([1, 2], 3))
# [(1,1,1), (1,1,2), (1,2,2), (2,2,2)]
```
