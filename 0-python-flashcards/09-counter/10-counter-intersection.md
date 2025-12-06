# Counter Intersection

**Q:** How do I get the minimum counts from two Counters?

**A:** Use & operator

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c & d  # Counter({'a': 1, 'b': 1})
```
