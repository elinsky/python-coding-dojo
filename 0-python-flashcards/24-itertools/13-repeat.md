# Repeat

**Q:** How do I repeat a value n times as an iterator?

**A:** Use itertools.repeat()

```python
from itertools import repeat

list(repeat(10, 3))   # [10, 10, 10]
list(repeat('x', 5))  # ['x', 'x', 'x', 'x', 'x']

# Infinite if no count given
# repeat(10)  # 10, 10, 10, 10, ...
```
