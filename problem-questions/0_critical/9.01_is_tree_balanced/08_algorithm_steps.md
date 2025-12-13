# Algorithm Steps

**Q:** What are the steps for checking if a tree is balanced (in order)?

**A:**
1. **Base case**: If tree is None, return (True, -1)
2. **Check left**: Recursively get left subtree result
3. **Early return**: If left not balanced, return immediately
4. **Check right**: Recursively get right subtree result
5. **Early return**: If right not balanced, return immediately
6. **Check current**: Is `abs(left.height - right.height) <= 1`?
7. **Compute height**: `max(left.height, right.height) + 1`
8. **Return**: (is_balanced, height)
