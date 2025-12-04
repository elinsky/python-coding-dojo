# Convert Iteration to Recursion

**Q:** How do I convert a loop to recursion?

**A:** Loop variable becomes parameter, loop body becomes recursive call

```python
# Iterative
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Recursive equivalent
def sum_recursive(n, total=0):
    if n == 0:
        return total
    return sum_recursive(n - 1, total + n)
```
