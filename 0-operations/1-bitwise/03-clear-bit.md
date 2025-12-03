# Q: How do I clear bit at position i?

# A: AND with NOT of (1 shifted left by i)

```python
x & ~(1 << i)
```
