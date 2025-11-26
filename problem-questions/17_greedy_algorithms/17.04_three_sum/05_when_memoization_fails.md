# When Memoization Falls Short

**Q:** Why is recursive + memoization not optimal for 3-sum?

**A:** The complexity is O(n × t) where t is the target sum.

If t is huge (like billions), this is much worse than O(n²). The memoization state space depends on the target value, not just the array size.

The reduction approach (3-sum → 2-sum) depends only on n, making it more robust.
