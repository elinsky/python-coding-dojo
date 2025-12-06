# Iterator Slice

**Q:** How do I slice an iterator (like list slicing)?

**A:** Use itertools.islice()

```python
from itertools import islice

list(islice('ABCDEFG', 2))      # first 2: ['A', 'B']
list(islice('ABCDEFG', 2, 4))   # [2:4]: ['C', 'D']
list(islice('ABCDEFG', 2, None)) # [2:]: ['C', 'D', 'E', 'F', 'G']
list(islice('ABCDEFG', 0, 5, 2)) # [0:5:2]: ['A', 'C', 'E']
```

Note: No negative indices supported
