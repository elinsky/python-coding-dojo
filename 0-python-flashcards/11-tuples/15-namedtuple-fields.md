# Get Named Tuple Fields

**Q:** How do I get the field names from a namedtuple?

**A:** Use _fields attribute

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Point._fields  # ('x', 'y')

# Extend namedtuple
Point3D = namedtuple('Point3D', Point._fields + ('z',))
```
