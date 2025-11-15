# Calculate Middle Index (Overflow Safe)

**Q:** How do I calculate the middle index (avoiding overflow)?

**A:** Add left to half the distance

```python
mid = left + (right - left) // 2
```
