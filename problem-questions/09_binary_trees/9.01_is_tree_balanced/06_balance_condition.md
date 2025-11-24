# Balance Condition

**Q:** How do you check if the current node is balanced (assuming both subtrees are balanced)?

**A:** `is_balanced = abs(left_result.height - right_result.height) <= 1`

The absolute height difference must be at most 1.
