# Shrinking Subarray Invariant

**Q:** What is the shrinking subarray invariant pattern?

**A:** Maintain a subarray guaranteed to contain the solution, shrink from one end based on comparisons.

```python
# Pattern for two-sum in sorted array:
left, right = 0, len(A) - 1
while left <= right:
    # Invariant: if solution exists, it's in A[left:right+1]
    if check(left, right):
        return found
    elif need_larger():
        left += 1  # Can't be in left
    else:
        right -= 1  # Can't be in right
```
