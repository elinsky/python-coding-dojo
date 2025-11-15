# Check if Bit is Set

**Q:** How do I check if bit k is set?

**A:** AND with shifted 1

```python
x & (1 << k)
```
