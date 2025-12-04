# Loop Condition and Termination

**Q:** What's the loop condition and what's true when it terminates?

**A:** `while left <= right`. Terminates when `left > right` (unchecked region is empty). At that point:
- Everything `< left` is valid
- Everything `> right` is invalid
- Since `left = right + 1`, there's no gap — you've checked everything
