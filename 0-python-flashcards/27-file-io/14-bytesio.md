# BytesIO (In-Memory Binary)

**Q:** How do I create a file-like object in memory (binary)?

**A:** Use io.BytesIO

```python
from io import BytesIO

# Create in-memory binary stream
buffer = BytesIO()
buffer.write(b'\x00\x01\x02\x03')

# Get content
buffer.seek(0)
data = buffer.read()  # b'\x00\x01\x02\x03'

# Or get all content
buffer.getvalue()  # b'\x00\x01\x02\x03'
```

Useful for processing binary data without temp files.
