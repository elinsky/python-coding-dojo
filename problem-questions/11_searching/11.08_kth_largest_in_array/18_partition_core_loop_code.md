# Partition Around Pivot: Core Loop Action (Code)

**Q:** What exactly happens inside the loop when processing `A[i]`?

**A:**
```python
if comp(A[i], pivot_value):
    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
    new_pivot_idx += 1
# else: do nothing (just advance i via the loop)
```
