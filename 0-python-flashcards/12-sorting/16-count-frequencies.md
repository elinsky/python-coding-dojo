# Count Frequencies

**Q:** How do I count element frequencies?

**A:** Use Counter from collections

```python
from collections import Counter

freq = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})

freq.most_common(2)  # [(3, 3), (2, 2)]
```
