# Simple Recursion Template

**Q:** What's the simplest template for tree recursion?

**A:** Three parts:

```python
def solve(tree):
    # 1. BASE CASE - simplest input (usually None)
    if not tree:
        return <base_value>

    # 2. RECURSIVE CALLS - get results from children
    left_result = solve(tree.left)
    right_result = solve(tree.right)

    # 3. COMBINE - put left and right together for current node
    return combine(left_result, right_result, tree.data)
```

**That's it. You only need 2 cases:**
- Base case: `if not tree`
- Everything else: recursive calls + combine