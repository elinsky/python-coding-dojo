# Max on Empty Stack

**Q:** For stack with max: what should max() return on an empty stack?

**A:** Throw an exception (e.g., raise an error). There is no valid max for an empty stack.

Note: Returning 0 as a default creates a subtle bug - negative elements will compare against this phantom 0 and incorrectly keep it as the max.
