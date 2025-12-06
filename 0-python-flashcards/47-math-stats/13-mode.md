# Mode

**Q:** How do I find the most common value?

**A:** Use statistics.mode() or statistics.multimode()

```python
from statistics import mode, multimode

mode([1, 2, 2, 3, 3, 3])     # 3
mode(['a', 'b', 'b', 'c'])   # 'b'

# Multiple modes
multimode([1, 1, 2, 2, 3])   # [1, 2]
```
