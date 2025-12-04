# Get Most Common Elements

**Q:** How do I get the n most common elements from a Counter? What is the time complexity?

**A:** Use most_common(n) method. Time: O(n log k) where k is total elements

```python
c = Counter([1, 1, 1, 2, 2, 3])
c.most_common(2)  # [(1, 3), (2, 2)]
c.most_common()   # All elements, most to least common
```
