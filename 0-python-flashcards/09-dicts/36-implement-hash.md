# Implement Hash for Custom Class

**Q:** How do I make a custom class hashable (usable as dict key)? (e.g. a Point class with x and y attributes)

**A:** Implement __hash__ and __eq__ methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```
