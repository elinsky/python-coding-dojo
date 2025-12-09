# Set Symmetric Difference Update (In-place)

**Q:** How do I keep only elements in either set but not both (in-place)?

**A:** Use ^= operator or symmetric_difference_update()

```python
s ^= t
s.symmetric_difference_update(t)
```
