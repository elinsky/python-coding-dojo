# 2-Sum with Hash Set

**Q:** How do you solve 2-sum in O(n) time using a hash set?

**A:**
1. Build a hash set of all elements
2. For each element `x`, check if `(target - x)` exists in the set
3. If found, return True

Time: O(n), Space: O(n)
