# Partition Around Pivot: Initial Rearrangement

**Q:** What initial operation is done to prepare for scanning?

**A:** The pivot element is swapped to the end of the range:
```python
A[pivot_idx], A[right] = A[right], A[pivot_idx]
```
This keeps the pivot out of the way while partitioning.
