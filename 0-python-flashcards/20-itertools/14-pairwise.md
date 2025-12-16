# Pairwise

**Q:** How do I iterate over consecutive pairs?

**A:** Use itertools.pairwise() (Python 3.10+)

```python
from itertools import pairwise

list(pairwise('ABCD'))
# [('A', 'B'), ('B', 'C'), ('C', 'D')]

list(pairwise([1, 2, 3, 4, 5]))
# [(1, 2), (2, 3), (3, 4), (4, 5)]
```
