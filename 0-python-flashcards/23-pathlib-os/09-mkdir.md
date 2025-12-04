# Create Directory

**Q:** How do I create a directory?

**A:** Use mkdir() with parents and exist_ok options

```python
from pathlib import Path

Path('new_dir').mkdir()
Path('a/b/c').mkdir(parents=True)         # create parent dirs
Path('dir').mkdir(exist_ok=True)          # no error if exists

# Or with os:
import os
os.mkdir('new_dir')
os.makedirs('a/b/c', exist_ok=True)       # create parent dirs
```
