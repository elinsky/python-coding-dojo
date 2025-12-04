# Counter Subtraction Operator

**Q:** How do I subtract Counters (positive counts only)?

**A:** Use - operator (keeps only positive counts)

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c - d  # Counter({'a': 2})  # b is dropped (would be -1)
```
