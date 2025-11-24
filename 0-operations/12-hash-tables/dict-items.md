# Get Dictionary Items

**Q:** How do I get all key-value pairs from a dictionary? What is the time complexity?

**A:** Use items() method. Time: O(1) to get view, O(n) to iterate

```python
items = d.items()
for key, value in d.items():
    # process key-value pair
```
