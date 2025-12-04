# Text vs Binary Mode

**Q:** What's the difference between text and binary mode?

**A:** Text handles encoding/newlines; binary is raw bytes

```python
# Text mode - returns str, handles encoding
with open('file.txt', 'r') as f:
    text = f.read()  # str

# Binary mode - returns bytes, no encoding
with open('file.txt', 'rb') as f:
    data = f.read()  # bytes

# Text mode converts line endings on Windows
# Binary mode keeps them as-is
```

Use text for .txt, .csv, .json; binary for images, .zip, etc.
