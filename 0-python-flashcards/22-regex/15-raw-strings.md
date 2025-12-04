# Raw Strings for Regex

**Q:** Why use raw strings (r'...') for regex patterns?

**A:** Prevents Python from interpreting backslashes

```python
import re

# Without raw string - need double backslash
re.search('\\d+', '123')

# With raw string - cleaner
re.search(r'\d+', '123')

# \b means word boundary, not backspace
re.search(r'\bword\b', 'a word here')
```
