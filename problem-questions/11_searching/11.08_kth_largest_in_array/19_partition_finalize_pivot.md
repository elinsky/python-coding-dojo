# Partition Around Pivot: Post-Loop Step (Finalize Pivot)

**Q:** What happens after the scan finishes?

**A:**

Swap the pivot (at `A[right]`) into place at `new_pivot_idx`:
```python
A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
```

Return `new_pivot_idx` (the pivot's final index).
