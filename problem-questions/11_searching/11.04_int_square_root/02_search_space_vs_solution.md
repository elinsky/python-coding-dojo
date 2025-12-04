# Search Space vs Solution Location

**Q:** Is the answer always within `[left, right]` during the search?

**A:** No. `[left, right]` contains only unchecked candidates. When you find a valid value, you keep searching to see if a better one exists. The answer is tracked implicitly as `left - 1` (the largest confirmed valid value), which is outside the search space.
