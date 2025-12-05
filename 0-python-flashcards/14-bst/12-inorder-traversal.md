# Inorder Traversal (Concept)

**Q:** How do you traverse a BST in sorted order?

**A:**
```
inorder(node):
    if node exists:
        inorder left
        visit node
        inorder right
```
