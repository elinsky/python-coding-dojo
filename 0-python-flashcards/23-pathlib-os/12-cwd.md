# Current Working Directory

**Q:** How do I get/change the current working directory?

**A:** Use Path.cwd() or os.getcwd()/os.chdir()

```python
from pathlib import Path
import os

cwd = Path.cwd()        # get as Path
cwd = os.getcwd()       # get as string

os.chdir('/new/path')   # change directory
```
