# Access Dictionary Value

**Q:** How do I access a value in a dictionary?

**A:** Use bracket notation or get() method

```python
value = d[key]  # Raises KeyError if not found
value = d.get(key)  # Returns None if not found
value = d.get(key, default)  # Returns default if not found
```
