# Quickselect: Big Picture Strategy

**Q:** What's the big picture strategy for quickselect?

**A:** Use **partition + binary search** on indices. O(n) average time, O(1) space.

1. Partition the array around a pivot — pivot lands in its "final sorted position"
2. If pivot is at index k-1, we're done
3. Otherwise, search only the half that contains index k-1
4. Repeat until pivot lands at k-1

Each partition is O(n), but we halve the search space each time: n + n/2 + n/4 + ... = 2n = O(n).
