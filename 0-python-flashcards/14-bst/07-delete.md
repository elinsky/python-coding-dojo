# Delete Key (Concept)

**Q:** What's the approach to delete a key from a BST?

**A:**
```
search for the node

if no left child:
    return right child
if no right child:
    return left child

two children:
    find successor (min of right subtree)
    copy successor value to this node
    delete successor from right subtree
return node
```
