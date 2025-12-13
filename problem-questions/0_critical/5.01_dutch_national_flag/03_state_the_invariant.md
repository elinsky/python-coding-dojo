# State the Invariant

**Q:** State the invariant in English for each region.

**A:**
- `A[0:smaller]` → all < pivot
- `A[smaller:equal]` → all == pivot
- `A[equal:larger]` → unprocessed
- `A[larger:]` → all > pivot
