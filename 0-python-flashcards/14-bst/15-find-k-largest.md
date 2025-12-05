# Find k Largest Elements (Concept)

**Q:** What's the approach to find the k largest elements in a BST?

**A:**
```
use reverse inorder traversal (right, root, left)
    visit right subtree
    if count < k:
        add current node
    visit left subtree
stop early once k elements collected
```
