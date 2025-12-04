# Handling Encoding Errors

**Q:** How do I handle encoding errors when reading files?

**A:** Use the errors parameter

```python
# Ignore characters that can't be decoded
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace with placeholder
with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()  # bad chars become �

# Options: 'strict' (default), 'ignore', 'replace', 'backslashreplace'
```
