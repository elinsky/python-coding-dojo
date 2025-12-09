# Partition Around Pivot: Postcondition

**Q:** After `partition_around_pivot` returns, what is guaranteed about the array?

**A:**
- `A[left:pivot_idx]` → elements satisfying `comp(A[i], pivot_value)`
- `A[pivot_idx]` → pivot in final position
- `A[pivot_idx+1:right+1]` → elements NOT satisfying `comp`

(For k-th largest: "satisfying comp" = > pivot. For k-th smallest: "satisfying comp" = < pivot.)
