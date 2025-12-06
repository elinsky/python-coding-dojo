# Group By

**Q:** How do I group consecutive elements by a key?

**A:** Use itertools.groupby() (sort first for non-consecutive!)

```python
from itertools import groupby

data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
```

Important: groupby only groups consecutive elements!
