# Starmap

**Q:** How do I apply a function to pre-zipped argument tuples?

**A:** Use itertools.starmap()

```python
from itertools import starmap

list(starmap(pow, [(2, 5), (3, 2), (10, 3)]))
# [32, 9, 1000]

list(starmap(max, [(1, 2, 3), (4, 1, 5), (2, 2)]))
# [3, 5, 2]
```

starmap(f, [(a,b), (c,d)]) == [f(a,b), f(c,d)]
