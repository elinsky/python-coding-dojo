# Truncate

**Q:** How do I remove the decimal part (truncate toward zero)?

**A:** Use math.trunc()

```python
import math

math.trunc(3.7)   # 3
math.trunc(-3.7)  # -3  (different from floor!)

# Equivalent to int() for most cases
int(3.7)    # 3
int(-3.7)   # -3
```
