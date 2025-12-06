# Partial Function Application

**Q:** How do I create a function with some arguments pre-filled?

**A:** Use functools.partial()

```python
from functools import partial

new_func = partial(func, arg=value)
```
