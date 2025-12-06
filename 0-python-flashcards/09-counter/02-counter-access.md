# Access Counter Count

**Q:** How do I get the count of an element in a Counter?

**A:** Use bracket notation (returns 0 for missing keys, not KeyError)

```python
from collections import Counter

c = Counter([1, 2, 2, 3])
c[2]  # 2
c[99]  # 0 (not KeyError)
```
