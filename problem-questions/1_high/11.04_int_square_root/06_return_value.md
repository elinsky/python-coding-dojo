# Return Value

**Q:** What do you return and why?

**A:** Return `left - 1`. When the loop exits, `left` has moved one past the last valid value. So `left - 1` is the largest value where `mid * mid <= k`.
