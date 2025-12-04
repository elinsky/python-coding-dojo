# Mean (Average)

**Q:** How do I calculate the arithmetic mean?

**A:** Use statistics.mean() or statistics.fmean()

```python
from statistics import mean, fmean

mean([1, 2, 3, 4, 5])     # 3
mean([1.5, 2.5, 3.5])     # 2.5

# fmean is faster (always returns float)
fmean([1, 2, 3, 4, 5])    # 3.0
```
