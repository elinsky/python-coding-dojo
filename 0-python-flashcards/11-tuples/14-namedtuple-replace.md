# Create Modified Named Tuple

**Q:** How do I create a new namedtuple with some fields changed?

**A:** Use _replace() method (tuples are immutable)

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = p1._replace(x=5)  # Point(x=5, y=4)
# p1 unchanged
```
