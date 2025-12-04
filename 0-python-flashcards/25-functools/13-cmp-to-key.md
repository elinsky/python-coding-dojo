# Compare to Key

**Q:** How do I use old-style comparison functions with sorted()?

**A:** Use functools.cmp_to_key()

```python
from functools import cmp_to_key

def compare(a, b):
    # Old-style: return -1, 0, or 1
    return (a > b) - (a < b)

# Convert to key function
sorted([3, 1, 4, 1, 5], key=cmp_to_key(compare))
# [1, 1, 3, 4, 5]

# Useful for complex custom sorting logic
```
