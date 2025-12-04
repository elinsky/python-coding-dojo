# Updating Right Pointer

**Q:** When `mid * mid > k` (invalid), how do you update `right` and why?

**A:** `right = mid - 1`. The value `mid` is too large, so exclude it and search smaller values.
