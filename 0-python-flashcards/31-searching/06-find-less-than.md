# Find Rightmost Value Less Than x

**Q:** How do I find the rightmost value less than x?

**A:** Use bisect_left and go back one

```python
i = bisect.bisect_left(a, x)
if i:
    return a[i - 1]
```
