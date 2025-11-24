# Dictionary Pop

**Q:** How do I remove and return a value from a dictionary? What is the time complexity?

**A:** Use pop() method. Time: O(1) average

```python
value = d.pop(key)  # Raises KeyError if not found
value = d.pop(key, default_value)  # Returns default if not found
```
