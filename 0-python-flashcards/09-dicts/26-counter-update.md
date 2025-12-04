# Update Counter

**Q:** How do I add counts from an iterable to a Counter?

**A:** Use update() method (adds, not replaces)

```python
c = Counter(a=1)
c.update(['a', 'b', 'b'])  # Counter({'b': 2, 'a': 2})
c.update({'a': 3})  # Adds 3 more 'a's
```
