# Find Successor

**Q:** How do I find the successor (next larger key) of a node?

**A:** If right child exists, find min in right subtree

```python
def find_successor(node):
    # If right child exists, successor is leftmost in right subtree
    if node.right:
        return find_min(node.right)
    # Otherwise, need parent pointer to find ancestor
```
