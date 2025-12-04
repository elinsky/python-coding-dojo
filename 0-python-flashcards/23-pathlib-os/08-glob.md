# Glob Pattern Matching

**Q:** How do I find files matching a pattern?

**A:** Use glob() or rglob() for recursive

```python
from pathlib import Path

# All .txt files in directory
for p in Path('.').glob('*.txt'):
    print(p)

# All .py files recursively
for p in Path('.').rglob('*.py'):
    print(p)
```
