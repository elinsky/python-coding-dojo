# Implement Custom Hash and Equality

**Q:** How do I make a custom class hashable for use in sets/dicts? What must I ensure?

**A:** Define __hash__ and __eq__. Equal objects MUST have equal hash codes.

```python
class ContactList:
    def __init__(self, names):
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)
```
