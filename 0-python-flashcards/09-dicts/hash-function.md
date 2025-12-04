# Get Hash Code

**Q:** How do I get the hash code of an object? What is the time complexity?

**A:** Use hash() function. Time: Varies by object type

```python
h = hash(obj)
h = hash("string")
h = hash((1, 2, 3))  # Tuples are hashable
h = hash(frozenset([1, 2]))  # Frozensets are hashable
# Lists and sets are NOT hashable
```
