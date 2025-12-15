# Key Insight

**Q:** What's the key insight for reconstructing a binary tree from preorder and inorder traversals?

**A:**
- The first element of preorder is always the root
- Find that root's position in inorder
- Everything to its left in inorder is the left subtree
- Everything to its right in inorder is the right subtree
