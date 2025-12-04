# Check NaN and Infinity

**Q:** How do I check for NaN or infinity?

**A:** Use math.isnan() and math.isinf()

```python
import math

math.isnan(math.nan)    # True
math.isnan(float('nan')) # True
math.isnan(5.0)         # False

math.isinf(math.inf)    # True
math.isinf(float('inf')) # True
math.isinf(1e308)       # False
```

Note: nan != nan is True (NaN is not equal to itself)
