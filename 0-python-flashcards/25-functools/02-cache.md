# Simple Cache (Unbounded)

**Q:** How do I cache function results without size limit?

**A:** Use @functools.cache (Python 3.9+)

```python
from functools import cache

@cache
def expensive_func(x):
    # complex computation
    return x * x

# Equivalent to @lru_cache(maxsize=None)
```
