# Find LCA in BST

**Q:** How do I find the lowest common ancestor of two nodes in a BST?

**A:** Descend tree using BST property until split point

```python
def find_LCA(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree
```
