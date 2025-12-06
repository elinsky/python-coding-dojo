# Convert Recursion to Iteration

**Q:** How do I convert recursion to iteration?

**A:** Use explicit stack to mimic call stack (for non-tail recursion)

```python
# Recursive
def dfs_recursive(node):
    if not node:
        return
    process(node)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

# Iterative with stack
def dfs_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        process(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```
