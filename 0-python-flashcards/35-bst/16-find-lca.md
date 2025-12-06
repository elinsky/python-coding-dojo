# Find LCA in BST (Concept)

**Q:** What's the approach to find the lowest common ancestor of two nodes in a BST?

**A:**
```
given nodes s (smaller) and b (bigger):
while node.data not in [s.data, b.data]:
    if node.data < s.data:
        go right
    if node.data > b.data:
        go left
return node (the split point)
```
