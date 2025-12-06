# Simple Cache (Unbounded)

**Q:** How do I cache function results without size limit?

**A:** Use @functools.cache

```python
from functools import cache

@cache
def expensive_func(x):
    ...
```
