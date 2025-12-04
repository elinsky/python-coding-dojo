# LRU Cache with Types

**Q:** How do I cache different types separately?

**A:** Use lru_cache with typed=True

```python
from functools import lru_cache

@lru_cache(maxsize=128, typed=True)
def process(x):
    return x * 2

process(3)    # cached as int
process(3.0)  # cached separately as float
```

Without typed=True, 3 and 3.0 would share cache entry
