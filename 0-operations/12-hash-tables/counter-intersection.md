# Counter Intersection

**Q:** How do I get the minimum counts from two Counters? What is the time complexity?

**A:** Use & operator. Time: O(min(len(c), len(d)))

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
result = c & d  # Counter({'a': 1, 'b': 1})
```
