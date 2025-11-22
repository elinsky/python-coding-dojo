# How do you swap bits at positions i and j?

```python
# Only swap if bits are different
if ((x >> i) & 1) != ((x >> j) & 1):
    x ^= (1 << i) | (1 << j)
```
