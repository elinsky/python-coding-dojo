# 2-Sum with Two Pointers

**Q:** How do you solve 2-sum in O(n) time with O(1) space?

**A:** Use two pointers on a **sorted** array:
1. Left pointer at start, right pointer at end
2. If sum < target: move left pointer right (need bigger)
3. If sum > target: move right pointer left (need smaller)
4. If sum == target: found it

Time: O(n), Space: O(1) (but requires sorted input)
