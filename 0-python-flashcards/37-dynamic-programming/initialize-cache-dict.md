# Initialize Cache Dictionary

**Q:** How do you initialize a cache for memoization using a dictionary?

**A:** Use a dict with default parameter or empty dict

```python
# As default parameter (persistent across calls)
def fib(n, cache={}):
    pass

# Or initialize in function
cache = {}
```
