# Set Intersection

**Q:** How do I get common elements between two sets? What is the time complexity?

**A:** Use & operator or intersection() method. Time: O(min(len(s), len(t))) average

```python
common = s & t
common = s.intersection(t)
```
