# Product and Sum

**Q:** How do I compute product/sum of a sequence?

**A:** Use math.prod() and sum() builtin

```python
import math

# Product
math.prod([1, 2, 3, 4])  # 24
math.prod([2, 2, 2])     # 8

# Sum (builtin)
sum([1, 2, 3, 4])        # 10
sum([1, 2, 3], 10)       # 16 (with start value)

# For precise float sums
math.fsum([0.1, 0.2, 0.3])  # 0.6 (more accurate)
```
