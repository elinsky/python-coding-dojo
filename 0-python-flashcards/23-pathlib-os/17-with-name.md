# Change Filename

**Q:** How do I change just the filename portion of a path?

**A:** Use with_name() or with_stem()

```python
from pathlib import Path

p = Path('/home/user/old.txt')
p.with_name('new.txt')    # Path('/home/user/new.txt')
p.with_stem('new')        # Path('/home/user/new.txt')
```
