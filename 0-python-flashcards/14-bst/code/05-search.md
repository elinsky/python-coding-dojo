# Search BST Iteratively

**Q:** How do I search for a key in a BST? Return the node if found, None otherwise.

```python
def search_bst(tree, key):
```

**A:** Compare and move left or right until found or null

```python
def search_bst(tree, key):
    while tree and tree.data != key:
        tree = tree.left if key < tree.data else tree.right
    return tree
```
