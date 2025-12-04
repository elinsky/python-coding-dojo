# Regex Find Iterator

**Q:** How do I iterate over all matches with match info?

**A:** Use re.finditer() - returns iterator of Match objects

```python
import re

for m in re.finditer(r'\d+', 'a1 b22 c333'):
    print(m.group(), m.start(), m.end())
# '1' 1 2
# '22' 4 6
# '333' 8 11
```
