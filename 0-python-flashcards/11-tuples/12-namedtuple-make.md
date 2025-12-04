# Create Named Tuple from Iterable

**Q:** How do I create a namedtuple from an existing iterable?

**A:** Use _make() class method

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
coords = [3, 4]
p = Point._make(coords)  # Point(x=3, y=4)
```
