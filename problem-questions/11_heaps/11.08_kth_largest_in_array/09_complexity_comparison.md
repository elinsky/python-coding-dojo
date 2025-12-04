# Complexity Comparison

**Q:** Compare the time/space complexity of heap vs quickselect for k-th largest.

**A:**

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Min-heap | O(n log k) | O(k) | Guaranteed, doesn't modify input |
| Quickselect | O(n) avg, O(n^2) worst | O(1) | Modifies array, random pivot needed |

Heap is often preferred in practice: predictable, non-destructive, works on streams.
