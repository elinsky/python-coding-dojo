# Find Predecessor

**Q:** How do I find the predecessor (next smaller key) of a node?

**A:** If left child exists, find max in left subtree

```python
def find_predecessor(node):
    # If left child exists, predecessor is rightmost in left subtree
    if node.left:
        return find_max(node.left)
    # Otherwise, need parent pointer to find ancestor
```
