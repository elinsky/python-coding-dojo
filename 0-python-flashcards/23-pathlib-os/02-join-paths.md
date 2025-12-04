# Join Paths

**Q:** How do I join path components?

**A:** Use / operator or joinpath()

```python
from pathlib import Path

p = Path('/home/user')
full = p / 'documents' / 'file.txt'
# /home/user/documents/file.txt

# Or with os.path:
import os
path = os.path.join('/home/user', 'documents', 'file.txt')
```
