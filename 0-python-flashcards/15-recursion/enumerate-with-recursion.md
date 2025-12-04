# Enumerate Solutions with Recursion

**Q:** How do I enumerate all solutions using recursion?

**A:** Build solution incrementally, collect when complete

```python
def enumerate_all(n):
    result = []

    def helper(partial_solution):
        if is_complete(partial_solution):
            result.append(partial_solution.copy())
            return

        for choice in get_choices():
            partial_solution.append(choice)
            helper(partial_solution)
            partial_solution.pop()  # Backtrack

    helper([])
    return result
```
