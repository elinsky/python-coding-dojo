# Regex Find All Matches

**Q:** How do I find all occurrences of a pattern?

**A:** Use re.findall() - returns list of strings

```python
import re

re.findall(r'\d+', 'a1 b22 c333')
# ['1', '22', '333']
```
