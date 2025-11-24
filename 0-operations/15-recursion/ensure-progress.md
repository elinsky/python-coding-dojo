# Ensure Progress Toward Base Case

**Q:** How do I ensure recursion converges to a solution?

**A:** Each recursive call must make progress toward the base case

```python
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)  # y gets smaller each call
```
