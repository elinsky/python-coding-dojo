# Counter Addition

**Q:** How do I add two Counters together? What is the time complexity?

**A:** Use + operator (keeps only positive counts). Time: O(n + m)

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
result = c + d  # Counter({'a': 4, 'b': 3})
```
