# Recursion Space Complexity

**Q:** How do I calculate space complexity of recursion?

**A:** Maximum depth of call stack × space per call

```python
# Space: O(n) - call stack depth is n
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Space: O(log n) - call stack depth is log n
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```
