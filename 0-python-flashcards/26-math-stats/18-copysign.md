# Copy Sign

**Q:** How do I copy the sign from one number to another?

**A:** Use math.copysign()

```python
import math

math.copysign(5, -1)    # -5.0
math.copysign(-5, 1)    # 5.0
math.copysign(3.14, -0.0)  # -3.14
```
