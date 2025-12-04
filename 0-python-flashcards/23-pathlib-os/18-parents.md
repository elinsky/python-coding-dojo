# Get Parent Directories

**Q:** How do I get parent directories?

**A:** Use parent or parents

```python
from pathlib import Path

p = Path('/home/user/data/file.txt')
p.parent              # Path('/home/user/data')
p.parent.parent       # Path('/home/user')

list(p.parents)       # [Path('/home/user/data'),
                      #  Path('/home/user'),
                      #  Path('/home'),
                      #  Path('/')]
```
