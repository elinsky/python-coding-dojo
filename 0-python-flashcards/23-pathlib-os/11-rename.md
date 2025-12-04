# Rename/Move File

**Q:** How do I rename or move a file?

**A:** Use rename() or replace()

```python
from pathlib import Path

Path('old.txt').rename('new.txt')
Path('file.txt').rename('subdir/file.txt')  # move

# replace() overwrites existing
Path('a.txt').replace('b.txt')

# Or with os:
import os
os.rename('old.txt', 'new.txt')
```
