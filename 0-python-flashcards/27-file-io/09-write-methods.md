# Write Methods

**Q:** What are the different ways to write to a file?

**A:** write() and writelines()

```python
with open('output.txt', 'w') as f:
    # Write string
    f.write('Hello\n')
    f.write('World\n')

    # Write multiple strings (no newlines added!)
    lines = ['line1\n', 'line2\n', 'line3\n']
    f.writelines(lines)
```

Note: writelines() does NOT add newlines automatically.
