# Total Ordering

**Q:** How do I implement all comparison operators from just one?

**A:** Use @functools.total_ordering class decorator

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

# Now <, >, <=, >= all work automatically
```

Requires: __eq__ plus one of __lt__, __le__, __gt__, __ge__
