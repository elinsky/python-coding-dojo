# Get Total of All Counts

**Q:** How do I get the sum of all counts in a Counter?

**A:** Use total() method (Python 3.10+) or sum(c.values())

```python
c = Counter(a=3, b=2, c=1)
c.total()  # 6 (Python 3.10+)
sum(c.values())  # 6 (all versions)
```
