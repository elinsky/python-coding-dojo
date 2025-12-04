# Regex Anchors

**Q:** How do I match start/end of string?

**A:** Use ^ for start, $ for end

```python
import re

re.search(r'^hello', 'hello world')  # Match
re.search(r'^hello', 'say hello')    # None

re.search(r'world$', 'hello world')  # Match
re.search(r'world$', 'world tour')   # None
```
