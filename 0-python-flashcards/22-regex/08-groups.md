# Regex Capture Groups

**Q:** How do I capture parts of a match?

**A:** Use parentheses () for groups, then group() or groups()

```python
import re

m = re.search(r'(\d+)-(\d+)', 'phone: 123-4567')
m.group()   # '123-4567' (full match)
m.group(1)  # '123'
m.group(2)  # '4567'
m.groups()  # ('123', '4567')
```
