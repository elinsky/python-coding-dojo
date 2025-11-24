# Directed Recursion

**Q:** What is directed recursion and when should I use it?

**A:** Only recurse on valid/promising paths (prune invalid choices early)

```python
# Instead of generating all, then filtering
def generate_all_then_filter(n):
    all_solutions = generate_all(n)
    return [s for s in all_solutions if is_valid(s)]

# Directed: check validity before recursing
def directed_generate(n, partial=[]):
    if len(partial) == n:
        result.append(partial.copy())
        return

    for choice in get_choices():
        if is_valid_choice(partial, choice):  # Check BEFORE recursing
            partial.append(choice)
            directed_generate(n, partial)
            partial.pop()
```
