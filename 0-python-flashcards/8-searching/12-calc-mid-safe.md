# Calculate Middle Index (Overflow Safe)

**Q:** How do I calculate middle index (overflow safe)?

**A:** Add left to half the distance

```python
mid = left + (right - left) // 2
```
