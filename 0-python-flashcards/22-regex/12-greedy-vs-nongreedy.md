# Greedy vs Non-Greedy

**Q:** How do I make quantifiers non-greedy (match minimum)?

**A:** Add ? after the quantifier

```python
import re

s = '<div>hello</div>'
re.search(r'<.*>', s).group()   # '<div>hello</div>' (greedy)
re.search(r'<.*?>', s).group()  # '<div>' (non-greedy)
```
