# Multiple Recursive Calls Pattern

**Q:** How do I handle problems requiring multiple recursive calls?

**A:** Make separate calls and combine results

```python
# Binary tree traversal
def process_tree(node):
    if not node:
        return base_value

    left_result = process_tree(node.left)
    right_result = process_tree(node.right)

    return combine(node.data, left_result, right_result)

# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  # Two calls, add results
```
