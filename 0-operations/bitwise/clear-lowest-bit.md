# Q: How do I clear/remove the lowest set bit?

# A: AND with (x - 1)

```python
x & (x - 1)
```
