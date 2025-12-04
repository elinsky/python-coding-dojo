# Q: How do I find positions where consecutive bits differ?

# A: XOR with right-shifted self

```python
x ^ (x >> 1)  # Each set bit marks where neighbors differ

# Example: x = 0b110 (6)
#   x >> 1 = 0b011 (3)
#   x ^ (x >> 1) = 0b101 (positions 0 and 2 have different neighbors)
```
