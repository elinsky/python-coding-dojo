# Walk Directory Tree

**Q:** How do I recursively traverse a directory tree?

**A:**

```python
import os

for dirpath, dirnames, filenames in os.walk('/path'):
```
