# Insert Key (Concept)

**Q:** What's the approach to insert a key into a BST?

**A:**
```
if tree is empty:
    return new node
if key is smaller:
    recurse left
else:
    recurse right
return node
```
