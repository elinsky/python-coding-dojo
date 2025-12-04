# Check if Tail Recursive

**Q:** How do I identify tail recursion?

**A:** Recursive call is the last operation (no work after it returns)

```python
# Tail recursive
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)  # Nothing after recursive call

# NOT tail recursive
def factorial_bad(n):
    if n == 0:
        return 1
    return n * factorial_bad(n - 1)  # Multiplication after recursive call
```
