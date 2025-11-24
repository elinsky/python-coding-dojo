# Get Dictionary Keys

**Q:** How do I get all keys from a dictionary? What is the time complexity?

**A:** Use keys() method. Time: O(1) to get view, O(n) to iterate

```python
keys = d.keys()
for key in d.keys():  # Or just: for key in d:
    # process key
```
