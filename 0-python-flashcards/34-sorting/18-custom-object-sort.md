# Sort Custom Objects

**Q:** How do I make a custom class sortable?

**A:** Implement __lt__ method or use key parameter

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

students.sort()  # Uses __lt__
# Or: students.sort(key=lambda s: s.gpa)
```
