# List Directory Contents

**Q:** How do I list files in a directory?

**A:** Use iterdir() or os.listdir()

```python
from pathlib import Path

for item in Path('.').iterdir():
    print(item.name)

# Or with os:
import os
for name in os.listdir('.'):
    print(name)
```
