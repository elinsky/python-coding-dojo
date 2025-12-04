# Sort Objects by Field

**Q:** How do I sort objects using a specific field?

**A:** Define __lt__ or use key parameter

```python
# Method 1: Define __lt__ in class
class Student:
    def __lt__(self, other):
        return self.name < other.name

students.sort()  # Uses __lt__

# Method 2: Use key parameter
students.sort(key=lambda s: s.grade_point_average)
```
