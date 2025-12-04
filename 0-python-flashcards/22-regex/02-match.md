# Regex Match

**Q:** How do I check if a string starts with a pattern?

**A:** Use re.match() - only matches at beginning

```python
import re

re.match(r'\d+', '42 apples')   # Match object
re.match(r'\d+', 'price: 42')   # None (doesn't start with digit)
```
