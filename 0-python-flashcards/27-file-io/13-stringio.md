# StringIO (In-Memory Text)

**Q:** How do I create a file-like object in memory (text)?

**A:** Use io.StringIO

```python
from io import StringIO

# Create in-memory text stream
buffer = StringIO()
buffer.write('Hello\n')
buffer.write('World\n')

# Get content
buffer.seek(0)
content = buffer.read()  # 'Hello\nWorld\n'

# Or get all content
buffer.getvalue()  # 'Hello\nWorld\n'
```

Useful for testing and when APIs expect file objects.
