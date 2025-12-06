# Check If Result is Cached

**Q:** How do you check if a result is already in the cache before computing?

**A:** Use `in` operator or check for sentinel value

```python
# Method 1: Using 'in'
if n not in cache:
    cache[n] = compute_result(n)

# Method 2: Using sentinel (-1)
if cache[i][j] == -1:
    cache[i][j] = compute_result(i, j)
```
