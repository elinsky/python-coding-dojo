# Find Maximum Key

**Q:** How do I find the maximum key in a BST? Return the node (or None if empty).

```python
def find_max(tree):
```

**A:** Go to the rightmost node

```python
def find_max(tree):
    while tree and tree.right:
        tree = tree.right
    return tree
```
