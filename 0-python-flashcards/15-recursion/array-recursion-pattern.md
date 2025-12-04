# Array/List Recursion Pattern

**Q:** What are common patterns for recursing on arrays/lists?

**A:** Process first element, recurse on rest OR use indices

```python
# Pattern 1: First + Rest (Pythonic, creates copies)
def sum_list(arr):
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])

# Pattern 2: Index-based (more efficient)
def sum_list_idx(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_list_idx(arr, i + 1)

# Pattern 3: Range-based
def sum_range(arr, left, right):
    if left > right:
        return 0
    return arr[left] + sum_range(arr, left + 1, right)
```
