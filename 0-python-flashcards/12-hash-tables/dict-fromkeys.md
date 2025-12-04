# Create Dict from Keys

**Q:** How do I create a dictionary from a sequence of keys with a default value? What is the time complexity?

**A:** Use dict.fromkeys() class method. Time: O(n)

```python
d = dict.fromkeys(['a', 'b', 'c'], 0)  # {'a': 0, 'b': 0, 'c': 0}
d = dict.fromkeys(range(5))  # {0: None, 1: None, ...}
```
