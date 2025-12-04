# Walk Directory Tree

**Q:** How do I recursively traverse a directory tree?

**A:** Use os.walk() - yields (dirpath, dirnames, filenames)

```python
import os

for dirpath, dirnames, filenames in os.walk('/path'):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        print(full_path)
```
