# Find Minimum Key

**Q:** How do I find the minimum key in a BST? Return the node (or None if empty).

```python
def find_min(tree):
```

**A:** Go to the leftmost node

```python
def find_min(tree):
    while tree and tree.left:
        tree = tree.left
    return tree
```
