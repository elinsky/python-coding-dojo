# Two Sum in Sorted Array

**Q:** How do you find two elements that sum to target in a sorted array?

**A:** Use two pointers (start and end), move based on sum comparison. Time: O(n), Space: O(1)

```python
i, j = 0, len(A) - 1
while i <= j:
    if A[i] + A[j] == target:
        return True
    elif A[i] + A[j] < target:
        i += 1  # Need larger sum
    else:
        j -= 1  # Need smaller sum
return False
```
