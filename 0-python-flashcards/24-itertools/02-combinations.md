# Combinations

**Q:** How do I get all r-length combinations without replacement?

**A:** Use itertools.combinations()

```python
from itertools import combinations

list(combinations('ABCD', 2))
# [('A','B'), ('A','C'), ('A','D'), ('B','C'), ('B','D'), ('C','D')]

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```
