# Update Dictionary from Another Dict

**Q:** How do I update a dictionary with key-value pairs from another dict? What is the time complexity?

**A:** Use update() method. Time: O(len(other))

```python
d1.update(d2)  # Adds/overwrites keys from d2 into d1
d1.update({'a': 1, 'b': 2})
```
