# LRU Cache

**Q:** How do I cache function results with size limit?

**A:** Use @functools.lru_cache()

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # or None for unlimited
def expensive_func(x, y):
    ...
```
