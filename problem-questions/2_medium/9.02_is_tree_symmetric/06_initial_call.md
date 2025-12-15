# Initial Call

**Q:** How do you call the helper from is_symmetric(tree)?

**A:** `return helper(tree, tree)` - start by comparing the tree against itself, which compares left vs right subtrees on first recursion.
