# Rotate Array Left

**Q:** How do I rotate array left by k positions?

**A:** Concatenate slice from k with slice to k

```python
A[k:] + A[:k]
```
