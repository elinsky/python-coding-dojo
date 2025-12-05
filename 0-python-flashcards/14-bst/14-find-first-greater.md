# Find First Greater Than k (Concept)

**Q:** What's the approach to find the first key greater than k in a BST?

**A:**
```
candidate = null
while node exists:
    if node.data > k:
        candidate = node
        go left (look for smaller match)
    else:
        go right (need larger value)
return candidate
```
