# Why Carry-Out Means All 9s

**Q:** In `plus_one`, why does a carry-out from the leftmost digit guarantee the original input was all 9s?

**A:** For a carry to propagate left, each digit must have been 9 (since 9+1=10 triggers a carry, but 8+1=9 stops it). So carry-out only happens for inputs like `[9]`, `[9,9]`, `[9,9,9]`, etc.
