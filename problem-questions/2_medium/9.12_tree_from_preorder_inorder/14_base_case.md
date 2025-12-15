# Base Case

**Q:** What is the base case for the helper function?

**A:** If the range is empty, return None.

`if preorder_start >= preorder_end or inorder_start >= inorder_end: return None`

The indices use half-open ranges like Python slicing: `[start, end)`. So `start == end` means zero elements.
