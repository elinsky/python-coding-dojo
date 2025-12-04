# Sort with attrgetter

**Q:** How do I sort objects by attribute using operator.attrgetter?

**A:** Use attrgetter('attr_name')

```python
from operator import attrgetter

students.sort(key=attrgetter('gpa'))
students.sort(key=attrgetter('gpa', 'name'))  # Multiple
students.sort(key=attrgetter('address.city'))  # Nested
```
