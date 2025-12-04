# Search BST Iteratively

**Q:** How do I search a BST iteratively?

**A:** Compare and move left or right until found or null

```python
def search_bst(tree, key):
    while tree and tree.data != key:
        tree = tree.left if key < tree.data else tree.right
    return tree
```
