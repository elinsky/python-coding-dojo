# Median

**Q:** How do I calculate the median?

**A:** Use statistics.median()

```python
from statistics import median, median_low, median_high

median([1, 3, 5])        # 3
median([1, 3, 5, 7])     # 4.0 (average of 3 and 5)

# Get actual data point for even-length
median_low([1, 3, 5, 7])  # 3
median_high([1, 3, 5, 7]) # 5
```
