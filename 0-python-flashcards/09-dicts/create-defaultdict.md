# Create DefaultDict

**Q:** How do I create a dictionary that returns a default value for missing keys? What is the time complexity?

**A:** Use collections.defaultdict with type. Time: O(1)

```python
from collections import defaultdict

d = defaultdict(list)  # Missing keys return []
d = defaultdict(int)   # Missing keys return 0
d = defaultdict(set)   # Missing keys return set()
```
