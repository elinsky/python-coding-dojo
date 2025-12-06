# Convert Comparison Function to Key

**Q:** How do I use an old-style comparison function?

**A:** Use functools.cmp_to_key()

```python
from functools import cmp_to_key

def compare(x, y):
    # Return negative if x < y, 0 if equal, positive if x > y
    return (x > y) - (x < y)

A.sort(key=cmp_to_key(compare))
```
