# Contiguous Subarrays

**Q:** Are the subtree elements always contiguous (next to each other) in both preorder and inorder arrays?

**A:** Yes. Both traversals keep subtrees together:
- Inorder groups by: `[left subtree] [root] [right subtree]`
- Preorder groups by: `[root] [left subtree] [right subtree]`

And this pattern repeats recursively:
- Inorder's `[left subtree]` breaks down into its own `[left] [root] [right]`
- Preorder's `[left subtree]` breaks down into its own `[root] [left] [right]`

This means you can track regions with start/end indices instead of copying arrays.
