# Helper Function Pattern

**Q:** How do I structure recursion with additional state/parameters?

**A:** Use nested helper function with extra parameters

```python
def solve(input_data):
    def helper(index, current_state):
        if index == len(input_data):
            return base_value
        # Recursive logic with state
        return helper(index + 1, updated_state)

    return helper(0, initial_state)
```
