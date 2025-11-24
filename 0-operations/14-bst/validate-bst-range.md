# Validate BST with Range

**Q:** How do I check if a binary tree is a valid BST?

**A:** Use range checking with recursion

```python
def is_binary_tree_bst(tree, low=float('-inf'), high=float('inf')):
    if not tree:
        return True
    elif not low <= tree.data <= high:
        return False
    return (is_binary_tree_bst(tree.left, low, tree.data)
            and is_binary_tree_bst(tree.right, tree.data, high))
```
