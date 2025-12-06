# Quantiles

**Q:** How do I calculate quartiles and percentiles?

**A:** Use statistics.quantiles()

```python
from statistics import quantiles

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Quartiles (default n=4)
quantiles(data)           # [2.75, 5.5, 8.25]

# Deciles (n=10)
quantiles(data, n=10)     # 9 cut points

# Percentiles (n=100)
quantiles(data, n=100)    # 99 cut points
```
