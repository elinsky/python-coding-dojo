# Get Counter Elements as Iterator

**Q:** How do I get an iterator over elements (repeating each count times)?

**A:** Use elements() method

```python
c = Counter(a=3, b=1)
list(c.elements())  # ['a', 'a', 'a', 'b']
```
