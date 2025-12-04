# Resolve Absolute Path

**Q:** How do I get the absolute path, resolving symlinks?

**A:** Use resolve()

```python
from pathlib import Path

p = Path('./data/../file.txt')
absolute = p.resolve()
# /full/path/to/file.txt

# Just make absolute without resolving symlinks:
absolute = p.absolute()
```
