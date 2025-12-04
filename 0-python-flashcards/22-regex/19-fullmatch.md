# Regex Full Match

**Q:** How do I check if an entire string matches a pattern?

**A:** Use re.fullmatch()

```python
import re

re.fullmatch(r'\d+', '123')     # Match
re.fullmatch(r'\d+', '123abc')  # None

# Equivalent to:
re.match(r'^\d+$', '123')
```
