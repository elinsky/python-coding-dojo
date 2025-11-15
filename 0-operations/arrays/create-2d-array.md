# Create 2D Array

**Q:** How do I create 2D array m×n initialized to 0?

**A:** Use list comprehension (NOT [[0]*n]*m)

```python
[[0] * n for _ in range(m)]  # correct
[[0] * n] * m                # WRONG - creates shallow copies
```
