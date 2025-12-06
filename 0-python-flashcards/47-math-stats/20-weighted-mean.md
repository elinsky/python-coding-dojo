# Weighted Mean

**Q:** How do I calculate a weighted average?

**A:** Use statistics.fmean() with weights

```python
from statistics import fmean

grades = [90, 80, 70]
weights = [0.5, 0.3, 0.2]  # weights must sum to 1 (or will normalize)

fmean(grades, weights)  # 83.0

# Manual calculation:
sum(g * w for g, w in zip(grades, weights)) / sum(weights)
```
