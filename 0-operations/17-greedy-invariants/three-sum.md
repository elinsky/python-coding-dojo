# Three Sum Pattern

**Q:** How do you find three elements that sum to target?

**A:** Sort array, fix one element, use two-sum on remaining. Time: O(n²)

```python
def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)

# For each element a, find if remaining two sum to t - a
```
