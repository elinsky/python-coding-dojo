# Structure of Recursive Function

**Q:** What's the template for structuring a tree recursive function?

**A:** Follow this pattern:

```python
def recursive_function(tree):
    # 1. BASE CASE - simplest input
    if not tree:
        return <trivial answer>

    # 2. RECURSIVE CALLS - get info from children
    left_result = recursive_function(tree.left)

    # 3. EARLY TERMINATION (optional) - if left tells you to stop
    if <should_stop>:
        return <early result>

    right_result = recursive_function(tree.right)

    # 4. EARLY TERMINATION (optional) - if right tells you to stop
    if <should_stop>:
        return <early result>

    # 5. PROCESS CURRENT - combine children's results
    current_result = <compute from left_result, right_result, tree.data>

    # 6. RETURN - what caller needs
    return current_result
```

**For is_tree_balanced:**
1. Base: `if not tree: return (True, -1)`
2. Left call: `left_result = check_balanced(tree.left)`
3. Early: `if not left_result.balanced: return (False, 0)`
4. Right call: `right_result = check_balanced(tree.right)`
5. Early: `if not right_result.balanced: return (False, 0)`
6. Process: `is_balanced = abs(left.height - right.height) <= 1`
7. Process: `height = max(left.height, right.height) + 1`
8. Return: `return (is_balanced, height)`

**Not all 6 steps are always needed** - omit early termination if not applicable.
