# Permutations

**Q:** How do I get all r-length permutations (order matters)?

**A:** Use itertools.permutations()

```python
from itertools import permutations

list(permutations('ABC', 2))
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

list(permutations([1, 2, 3]))  # all orderings
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
```
