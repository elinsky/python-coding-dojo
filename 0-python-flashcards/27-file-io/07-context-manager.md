# Context Manager (with statement)

**Q:** What's the best way to open files?

**A:** Use the 'with' statement - auto-closes file

```python
with open('data.txt', 'r') as f:
    content = f.read()
# File automatically closed here, even if exception occurs

# Multiple files
with open('in.txt') as fin, open('out.txt', 'w') as fout:
    fout.write(fin.read())
```

Always prefer 'with' over manual open/close.
