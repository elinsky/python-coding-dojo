# Three-Way Decision After Partition

**Q:** After partitioning, the pivot lands at index `p`. What are the three cases, and how do we update `left`/`right`?

**A:**
- `p == k-1` → **Found it!** Return `A[p]`
- `p > k-1` → k-th largest is further LEFT, so `right = p - 1`
- `p < k-1` → k-th largest is further RIGHT, so `left = p + 1`
