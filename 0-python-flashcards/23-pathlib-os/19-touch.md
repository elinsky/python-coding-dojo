# Create Empty File

**Q:** How do I create an empty file or update its timestamp?

**A:** Use touch()

```python
from pathlib import Path

Path('newfile.txt').touch()
Path('exists.txt').touch(exist_ok=True)  # no error if exists
```
