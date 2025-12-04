# Path Parts

**Q:** How do I extract parts of a path?

**A:** Use path properties

```python
from pathlib import Path

p = Path('/home/user/data/file.txt')
p.name      # 'file.txt'
p.stem      # 'file'
p.suffix    # '.txt'
p.parent    # Path('/home/user/data')
p.parts     # ('/', 'home', 'user', 'data', 'file.txt')
```
