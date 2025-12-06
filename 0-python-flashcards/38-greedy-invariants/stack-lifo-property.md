# Stack for LIFO Pattern

**Q:** When should you use a stack in greedy algorithms?

**A:** When insertions/deletions follow last-in-first-out order (e.g., blocking/unblocking elements).

```python
# Pattern: elements get blocked in reverse order of insertion
stack = []
for element in elements:
    while stack and is_blocked(stack[-1], element):
        process(stack.pop())  # Most recent blocked first
    stack.append(element)
```
