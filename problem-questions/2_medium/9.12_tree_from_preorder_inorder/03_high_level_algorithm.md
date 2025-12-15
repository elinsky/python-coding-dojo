# High Level Algorithm

**Q:** What's the high-level approach to reconstruct a tree from preorder and inorder?

**A:**
1. Identify the root (first element of preorder)
2. Split inorder into left and right subtrees using root's position
3. Recursively build left subtree
4. Recursively build right subtree
5. Return node connecting root to its children
