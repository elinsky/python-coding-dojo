# Space Optimization Approach

**Q:** In `plus_one`, why does the optimal solution use O(1) space instead of pre-allocating an extra digit?

**A:** The carry-out case (needing an extra digit) only happens when the input is all 9s (e.g., 999 → 1000). Since this is rare, modify in-place and handle the edge case specially rather than always paying O(n) extra space.
