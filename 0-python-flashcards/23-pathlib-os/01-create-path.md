# Create a Path

**Q:** How do I create a Path object?

**A:** Use Path() constructor

```python
from pathlib import Path

p = Path('/home/user/file.txt')
p = Path('data', 'file.txt')  # joins components
p = Path.cwd()                 # current directory
p = Path.home()                # home directory
```
