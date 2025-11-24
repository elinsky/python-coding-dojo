# Augmented BST

**Q:** What is an augmented BST?

**A:** BST with extra fields in nodes for efficient queries (e.g., size, count)

```python
# Example: Add size field to support range count queries
class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1  # Augmentation: count of nodes in subtree
```
