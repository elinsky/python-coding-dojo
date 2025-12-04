# Base Case Pattern

**Q:** What's the common pattern for handling base cases in DP recursion?

**A:** Check base cases first, then check cache, then recurse

```python
def dp(n):
    # Base cases first
    if n <= 1:
        return n

    # Check cache
    if n not in cache:
        # Recurse and cache
        cache[n] = dp(n-1) + dp(n-2)

    return cache[n]
```
