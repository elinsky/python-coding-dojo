# Why Random Pivot

**Q:** Why use a random pivot in quickselect?

**A:** To avoid O(n^2) worst case on sorted/nearly-sorted arrays.

With random pivots, the expected time is O(n) because we halve the search space on average:
- n + n/2 + n/4 + ... = 2n = O(n)
