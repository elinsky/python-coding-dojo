# Compile Regex Pattern

**Q:** How do I compile a regex for reuse?

**A:** Use re.compile() - returns Pattern object

```python
import re

pattern = re.compile(r'\d+')
pattern.search('price: 42')
pattern.findall('a1 b2 c3')
```

Tip: Compile when using the same pattern multiple times
