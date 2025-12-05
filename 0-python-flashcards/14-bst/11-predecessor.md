# Find Predecessor (Concept)

**Q:** What's the approach to find the predecessor (next smaller key) of a node?

**A:**
```
if left child exists:
    return max of left subtree

otherwise walk up:
    while node is parent's left child:
        move up
    return parent
```
