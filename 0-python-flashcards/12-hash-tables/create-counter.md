# Create Counter

**Q:** How do I create a Counter to count elements? What is the time complexity?

**A:** Use collections.Counter. Time: O(n) where n is number of elements

```python
from collections import Counter

c = Counter()
c = Counter([1, 2, 2, 3, 3, 3])
c = Counter("hello")  # Count characters
```
