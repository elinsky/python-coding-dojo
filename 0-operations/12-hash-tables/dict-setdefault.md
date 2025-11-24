# Dictionary setdefault

**Q:** How do I get a value and set it if key doesn't exist? What is the time complexity?

**A:** Use setdefault() method. Time: O(1) average

```python
value = d.setdefault(key, default_value)
# If key exists, returns d[key]
# If key doesn't exist, sets d[key] = default_value and returns it
```
