# Write File with Path

**Q:** How do I write a file using pathlib?

**A:** Use write_text() or write_bytes()

```python
from pathlib import Path

p = Path('output.txt')
p.write_text('Hello, World!')
p.write_bytes(b'\x00\x01\x02')
```
