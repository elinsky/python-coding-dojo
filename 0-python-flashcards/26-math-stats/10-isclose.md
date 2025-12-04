# Compare Floats

**Q:** How do I check if two floats are approximately equal?

**A:** Use math.isclose()

```python
import math

# Default rel_tol=1e-9
math.isclose(0.1 + 0.2, 0.3)  # True

# Custom tolerance
math.isclose(1.0, 1.001, rel_tol=0.01)  # True
math.isclose(1.0, 1.001, abs_tol=0.01)  # True

# Compare to zero (need abs_tol)
math.isclose(0.0, 0.0001, abs_tol=0.001)  # True
```
