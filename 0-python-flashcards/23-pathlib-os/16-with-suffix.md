# Change File Extension

**Q:** How do I change a file's extension?

**A:** Use with_suffix()

```python
from pathlib import Path

p = Path('data.txt')
new = p.with_suffix('.csv')    # Path('data.csv')
new = p.with_suffix('.tar.gz') # Path('data.tar.gz')
new = p.with_suffix('')        # Path('data') - remove extension
```
