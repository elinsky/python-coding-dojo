# Partition Around Pivot: Purpose

**Q:** What does `partition_around_pivot(left, right, pivot_idx)` do?

**A:** Reorders `A[left:right+1]` so that all elements satisfying `comp(x, pivot)` appear before the pivot, and all others appear after. Returns the pivot's final index.
