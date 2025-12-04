# Read Methods

**Q:** What are the different ways to read file content?

**A:** read(), readline(), readlines()

```python
with open('data.txt') as f:
    # Read entire file as string
    content = f.read()

    # Read n characters
    chunk = f.read(100)

    # Read one line
    line = f.readline()

    # Read all lines as list
    lines = f.readlines()  # ['line1\n', 'line2\n', ...]
```
