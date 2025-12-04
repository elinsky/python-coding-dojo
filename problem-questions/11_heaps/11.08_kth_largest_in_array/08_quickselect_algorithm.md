# Quickselect Algorithm

**Q:** Describe the quickselect algorithm for k-th largest.

**A:**
```
find_kth_largest(k, A):
    left, right = 0, len(A) - 1

    while left <= right:
        1. Pick random pivot in [left, right]
        2. p = partition(pivot, A, left, right)
        3. if p == k-1:   return A[p]
           elif p > k-1:  right = p - 1
           else:          left = p + 1
```
