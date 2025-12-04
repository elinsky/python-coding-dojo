# LRU Cache

**Q:** How do I cache function results with size limit?

**A:** Use @functools.lru_cache()

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(100)  # fast with caching
fib.cache_info()   # stats
fib.cache_clear()  # clear cache
```
