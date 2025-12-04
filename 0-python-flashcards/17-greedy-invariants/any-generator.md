# Using any() with Generator

**Q:** How do you check if any element satisfies a condition efficiently?

**A:** Use any() with generator expression - short-circuits on first True.

```python
# Check if any element has property:
return any(has_two_sum(A, t - a) for a in A)

# More efficient than:
# return True in [has_two_sum(A, t - a) for a in A]
```
