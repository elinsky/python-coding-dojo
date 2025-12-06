# Find Leftmost Value Equal to x

**Q:** How do I find the leftmost value exactly equal to x?

**A:** Use bisect_left and verify

```python
i = bisect.bisect_left(a, x)
if i < len(a) and a[i] == x:
    return i
```
