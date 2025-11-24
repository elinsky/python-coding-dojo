# Find k Largest Elements

**Q:** How do I find the k largest elements in a BST?

**A:** Use reverse inorder traversal (right, root, left)

```python
def find_k_largest_in_bst(tree, k):
    def helper(tree):
        if tree and len(result) < k:
            helper(tree.right)
            if len(result) < k:
                result.append(tree.data)
            helper(tree.left)

    result = []
    helper(tree)
    return result
```
