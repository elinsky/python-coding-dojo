# Absolute Value

**Q:** How do I get the absolute value?

**A:** Use abs() builtin or math.fabs() for floats

```python
import math

abs(-5)        # 5 (int)
abs(-5.5)      # 5.5 (float)

math.fabs(-5)  # 5.0 (always float)
math.fabs(-5.5) # 5.5
```

Tip: Use abs() for most cases; math.fabs() guarantees float return
