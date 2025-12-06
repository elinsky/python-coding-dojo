# Dictionary Pop Item

**Q:** How do I remove and return an arbitrary (key, value) pair?

**A:** Use popitem() method (LIFO order since Python 3.7+)

```python
key, value = d.popitem()  # Raises KeyError if empty
```
