# Regex Flags

**Q:** What are the common regex flags?

**A:** Flags modify pattern behavior:

```python
import re

re.IGNORECASE  # or re.I - case insensitive
re.MULTILINE   # or re.M - ^ and $ match line start/end
re.DOTALL      # or re.S - . matches newlines too
re.VERBOSE     # or re.X - allow whitespace/comments

re.search(r'hello', 'HELLO', re.IGNORECASE)
```
