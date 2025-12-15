# What Indices To Track

**Q:** To recurse on a subtree, what do you need to know about its position in the arrays?

**A:** For each subtree, you need start and end indices in both arrays:
- Where does this subtree start/end in preorder?
- Where does this subtree start/end in inorder?

That's 4 values: `preorder_start`, `preorder_end`, `inorder_start`, `inorder_end`
