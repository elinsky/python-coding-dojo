# Convert Named Tuple to Dict

**Q:** How do I convert a namedtuple to a dictionary?

**A:** Use _asdict() method

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
d = p._asdict()  # {'x': 3, 'y': 4}
```
