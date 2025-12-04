# Backtracking Pattern

**Q:** What is the basic backtracking pattern?

**A:** Try option, recurse, undo if it fails (restore state)

```python
def backtrack(state, options):
    if is_solution(state):
        result.append(state.copy())
        return

    for option in options:
        # Make choice
        state.append(option)

        # Recurse
        backtrack(state, new_options)

        # Undo choice (backtrack)
        state.pop()
```
