# Get Counter Elements as Iterator

**Q:** How do I get an iterator over elements (repeating each count times)? What is the time complexity?

**A:** Use elements() method. Time: O(n) total iterations where n is sum of counts

```python
c = Counter(a=3, b=1)
list(c.elements())  # ['a', 'a', 'a', 'b']
```
