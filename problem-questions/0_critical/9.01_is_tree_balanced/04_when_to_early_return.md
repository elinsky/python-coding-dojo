# When to Early Return

**Q:** When can you return early without checking the right subtree?

**A:** If `left_result.balanced == False`

Once you know the left subtree is unbalanced, the entire tree is unbalanced. No need to check the right side.

Same applies after checking right subtree - return immediately if unbalanced.
