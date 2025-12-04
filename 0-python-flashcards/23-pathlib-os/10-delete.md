# Delete File or Directory

**Q:** How do I delete a file or empty directory?

**A:** Use unlink() for files, rmdir() for empty dirs

```python
from pathlib import Path

Path('file.txt').unlink()               # delete file
Path('file.txt').unlink(missing_ok=True) # no error if missing
Path('empty_dir').rmdir()               # delete empty directory

# Or with os:
import os
os.remove('file.txt')
os.rmdir('empty_dir')
```
