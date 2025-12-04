# Cache Management

**Q:** How do I inspect and clear function caches?

**A:** Use cache_info() and cache_clear()

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(30)
print(fib.cache_info())
# CacheInfo(hits=28, misses=31, maxsize=100, currsize=31)

fib.cache_clear()  # clear all cached values
```
