# Active Pillars Pattern

**Q:** What is the "active pillars" pattern in greedy algorithms?

**A:** Track elements not yet "blocked" by later elements, typically using a stack.

```python
# Common pattern:
stack = []
for i, element in enumerate(elements):
    while stack and should_block(stack[-1], element):
        blocked = stack.pop()
        process(blocked, i)  # Know where it ends
    stack.append(i)
# Process remaining stack elements
```
