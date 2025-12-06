# Find Successor (Concept)

**Q:** What's the approach to find the successor (next larger key) of a node?

**A:**
```
if right child exists:
    return min of right subtree

otherwise walk up:
    while node is parent's right child:
        move up
    return parent
```
