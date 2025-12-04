# Create Counter

**Q:** How do I create a Counter to count elements?

**A:** Use collections.Counter

```python
from collections import Counter

c = Counter()
c = Counter([1, 2, 2, 3, 3, 3])
c = Counter("hello")  # Count characters
```
