# Create Named Tuple

**Q:** How do I create a tuple with named fields?

**A:** Use collections.namedtuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p = Point(x=3, y=4)

p.x  # 1
p[0]  # 1
```
