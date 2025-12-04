# Updating Left Pointer

**Q:** When `mid * mid <= k` (valid), how do you update `left` and why?

**A:** `left = mid + 1`. You've confirmed `mid` is valid, so search for something larger. You don't lose `mid` — it's implicitly tracked as `left - 1`.
