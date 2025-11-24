# Inorder Traversal

**Q:** How do I traverse a BST in sorted order?

**A:** Use inorder traversal (left, root, right)

```python
def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.data)
        inorder(tree.right)
```
