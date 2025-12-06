# Initialize 1D DP Table

**Q:** How do you initialize a 1D DP table of size n with default values?

**A:** Use list multiplication with initial value

```python
# Initialize with zeros
dp = [0] * n

# Initialize with infinity
dp = [float('inf')] * n

# Initialize with -1 (sentinel)
dp = [-1] * n

# First element different
dp = [1] + [0] * (n - 1)
```
