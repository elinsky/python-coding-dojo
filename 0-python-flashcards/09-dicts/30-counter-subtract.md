# Counter Subtract

**Q:** How do I subtract counts (allowing negative)?

**A:** Use subtract() method

```python
c = Counter(a=3, b=1)
c.subtract({'a': 1, 'b': 2})
# Counter({'a': 2, 'b': -1})
```
