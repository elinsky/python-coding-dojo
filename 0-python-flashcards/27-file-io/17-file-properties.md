# File Object Properties

**Q:** What properties can I check on a file object?

**A:** name, mode, closed

```python
with open('data.txt', 'r') as f:
    print(f.name)    # 'data.txt'
    print(f.mode)    # 'r'
    print(f.closed)  # False

print(f.closed)      # True (after with block)
```
