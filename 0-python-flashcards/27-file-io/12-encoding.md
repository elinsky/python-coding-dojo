# File Encoding

**Q:** How do I specify file encoding?

**A:** Use the encoding parameter

```python
# UTF-8 (recommended for most cases)
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Write with encoding
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello 你好')

# Other encodings
open('file.txt', encoding='latin-1')
open('file.txt', encoding='ascii')
```

Always specify encoding for cross-platform compatibility.
