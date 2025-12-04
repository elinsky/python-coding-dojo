# Count Element Frequencies

**Q:** How do I count frequencies for counting sort?

**A:** Use Counter from collections - O(n)

```python
from collections import Counter

# Count frequencies
freq = Counter(A)
# freq is dict-like: {element: count}

# Or manually
freq = {}
for x in A:
    freq[x] = freq.get(x, 0) + 1
```
