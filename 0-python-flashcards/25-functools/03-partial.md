# Partial Function Application

**Q:** How do I create a function with some arguments pre-filled?

**A:** Use functools.partial()

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

square(5)  # 25
cube(3)    # 27
```
