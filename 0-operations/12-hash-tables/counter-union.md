# Counter Union

**Q:** How do I get the maximum counts from two Counters? What is the time complexity?

**A:** Use | operator. Time: O(len(c) + len(d))

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
result = c | d  # Counter({'a': 3, 'b': 2})
```
