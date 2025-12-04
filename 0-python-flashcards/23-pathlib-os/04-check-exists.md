# Check if Path Exists

**Q:** How do I check if a file or directory exists?

**A:** Use exists(), is_file(), is_dir()

```python
from pathlib import Path

p = Path('/some/path')
p.exists()   # True if path exists
p.is_file()  # True if it's a file
p.is_dir()   # True if it's a directory

# Or with os.path:
import os
os.path.exists('/some/path')
os.path.isfile('/some/path')
os.path.isdir('/some/path')
```
