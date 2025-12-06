# Initialize 2D DP Table

**Q:** How do you initialize a 2D DP table of size n×m?

**A:** Use list comprehension (NOT multiplication for 2D!)

```python
# CORRECT: Each row is a separate list
dp = [[0] * m for _ in range(n)]

# WRONG: All rows reference same list!
dp = [[0] * m] * n  # DON'T DO THIS

# Initialize with -1
dp = [[-1] * m for _ in range(n)]
```
