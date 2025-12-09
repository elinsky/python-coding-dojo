# Partition Around Pivot: State the Invariant

**Q:** State the invariant for each region during `partition_around_pivot`.

**A:**
- `A[left:new_pivot_idx]` → elements satisfying `comp` (preferred side)
- `A[new_pivot_idx:i]` → elements NOT satisfying `comp`
- `A[i:right]` → unprocessed elements
- `A[right]` → pivot temporarily parked at end

That's the core invariant — it's what stays true every iteration of the loop.
