# Validate BST (Concept)

**Q:** What's the approach to check if a binary tree is a valid BST?

**A:**
```
validate(node, low, high):
    if node is null:
        return true
    if node.data not in [low, high]:
        return false
    return validate(left, low, node.data)
       and validate(right, node.data, high)
```
