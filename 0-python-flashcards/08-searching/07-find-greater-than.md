# Find Leftmost Value Greater Than x

**Q:** How do I find the leftmost value greater than x?

**A:** Use bisect_right

```python
i = bisect.bisect_right(a, x)
if i < len(a):
    return a[i]
```
