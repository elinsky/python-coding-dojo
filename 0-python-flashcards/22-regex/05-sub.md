# Regex Substitute

**Q:** How do I replace all pattern matches?

**A:** Use re.sub(pattern, replacement, string)

```python
import re

re.sub(r'\d+', 'X', 'a1 b22 c333')
# 'aX bX cX'

# With count limit
re.sub(r'\d+', 'X', 'a1 b22 c333', count=2)
# 'aX bX c333'
```
