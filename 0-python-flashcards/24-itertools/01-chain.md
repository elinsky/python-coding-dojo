# Chain Iterables

**Q:** How do I concatenate multiple iterables into one?

**A:** Use itertools.chain()

```python
from itertools import chain

list(chain([1, 2], [3, 4], [5]))
# [1, 2, 3, 4, 5]

list(chain('ABC', 'DEF'))
# ['A', 'B', 'C', 'D', 'E', 'F']
```
