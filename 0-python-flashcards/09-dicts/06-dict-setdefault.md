# Dictionary setdefault

**Q:** How do I get a value and set it if key doesn't exist?

**A:** Use setdefault() method

```python
value = d.setdefault(key, default_value)
# If key exists, returns d[key]
# If not, sets d[key] = default_value and returns it
```
