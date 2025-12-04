# Regex Sub with Function

**Q:** How do I use a function to compute replacements?

**A:** Pass a function as the replacement argument

```python
import re

def double(m):
    return str(int(m.group()) * 2)

re.sub(r'\d+', double, 'a1 b2 c3')
# 'a2 b4 c6'
```
