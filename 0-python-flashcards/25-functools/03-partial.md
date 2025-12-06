# Partial Function Application

**Q:** How do I create a function with some arguments pre-filled? (e.g. use pow to create square)

**A:** Use functools.partial()

```python
from functools import partial

square = partial(pow, exp=2)
square(5)  # 25
```
