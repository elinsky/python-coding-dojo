# Partial Square

**Q:** How do I use partial to create a square function from pow?

**A:**
```python
from functools import partial

square = partial(pow, exp=2)
square(5)  # 25
```
