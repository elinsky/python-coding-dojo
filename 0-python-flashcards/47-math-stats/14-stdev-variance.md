# Standard Deviation and Variance

**Q:** How do I calculate standard deviation and variance?

**A:** Use stdev/variance (sample) or pstdev/pvariance (population)

```python
from statistics import stdev, variance, pstdev, pvariance

data = [2, 4, 4, 4, 5, 5, 7, 9]

# Sample (n-1 denominator) - use for samples
stdev(data)       # 2.138...
variance(data)    # 4.571...

# Population (n denominator) - use when data is entire population
pstdev(data)      # 2.0
pvariance(data)   # 4.0
```
