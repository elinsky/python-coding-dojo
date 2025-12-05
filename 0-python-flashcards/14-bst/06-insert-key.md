# Insert Key in BST

**Q:** How do I insert a key into a BST? Return the (possibly new) root.

```python
def insert(tree, key):
```

**A:** Find the correct position and insert as leaf

```python
def insert(tree, key):
    if not tree:
        return BSTNode(key)
    if key < tree.data:
        tree.left = insert(tree.left, key)
    else:
        tree.right = insert(tree.right, key)
    return tree
```
