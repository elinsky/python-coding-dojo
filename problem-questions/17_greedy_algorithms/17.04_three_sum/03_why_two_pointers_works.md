# Why Two Pointers Works

**Q:** Why can you eliminate candidates without checking all pairs in the two-pointer approach?

**A:** In a sorted array, if `A[left] + A[right]` is too small, then `A[left] + anything_smaller_than_A[right]` is also too small.

So moving the left pointer right (to a bigger value) is the only way to increase the sum. You never miss a valid pair because impossibilities are eliminated, not valid solutions.
