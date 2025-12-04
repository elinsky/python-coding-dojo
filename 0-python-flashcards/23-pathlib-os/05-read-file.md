# Read File with Path

**Q:** How do I read a file using pathlib?

**A:** Use read_text() or read_bytes()

```python
from pathlib import Path

p = Path('data.txt')
content = p.read_text()           # returns string
content = p.read_text('utf-8')    # with encoding
data = p.read_bytes()             # returns bytes
```
