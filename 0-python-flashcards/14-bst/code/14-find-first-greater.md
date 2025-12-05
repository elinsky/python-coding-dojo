# Find First Greater Than k

**Q:** How do I find the first key greater than k in a BST?

**A:** Track candidate and update while descending

```python
def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far
```
