# Delete Key from BST

**Q:** How do I delete a key from a BST?

**A:** Handle 3 cases: no child, one child, two children

```python
def delete(tree, key):
    if not tree:
        return None
    if key < tree.data:
        tree.left = delete(tree.left, key)
    elif key > tree.data:
        tree.right = delete(tree.right, key)
    else:  # Found the node
        if not tree.left:
            return tree.right  # No left child
        elif not tree.right:
            return tree.left   # No right child
        # Two children: replace with min of right subtree
        min_node = find_min(tree.right)
        tree.data = min_node.data
        tree.right = delete(tree.right, min_node.data)
    return tree
```
