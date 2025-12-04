# pathlib vs os.path

**Q:** When should I use pathlib vs os.path?

**A:** pathlib is modern/object-oriented; os.path is string-based

```python
# pathlib (preferred for new code)
from pathlib import Path
p = Path('/home') / 'user' / 'file.txt'
content = p.read_text()
p.exists()

# os.path (legacy, but still common)
import os
p = os.path.join('/home', 'user', 'file.txt')
with open(p) as f:
    content = f.read()
os.path.exists(p)
```

Tip: Use pathlib for most cases; os for walk(), environ, chdir()
