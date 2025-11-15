# How do you swap bits at positions i and j?

```python
x ^ ((1 << i) | (1 << j))  # Toggle both bits simultaneously
```
