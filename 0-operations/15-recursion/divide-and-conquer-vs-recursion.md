# Divide and Conquer vs Recursion

**Q:** What distinguishes divide-and-conquer from general recursion?

**A:** D&C splits into 2+ independent subproblems of same type. Recursion is more general.

```python
# Divide and conquer: independent subproblems
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Independent
    right = merge_sort(arr[mid:])   # Independent
    return merge(left, right)

# Recursion (not D&C): single subproblem
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    # Only ONE recursive call happens
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```
