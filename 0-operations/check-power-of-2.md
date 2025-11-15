# Q: How do I check if x is a power of 2?

# A: Check if clearing lowest set bit gives 0 (and x != 0)

```python
x & (x - 1) == 0
```
