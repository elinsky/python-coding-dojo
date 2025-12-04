# Q: How do I isolate the lowest set bit?

# A: AND with negative (two's complement)

```python
x & -x
```
