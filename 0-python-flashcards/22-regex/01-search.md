# Regex Search

**Q:** How do I find a pattern anywhere in a string?

**A:** Use re.search() - returns Match object or None

```python
import re

match = re.search(r'\d+', 'price: 42 dollars')
if match:
    print(match.group())  # '42'
```
