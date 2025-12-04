# Custom Character Sets

**Q:** How do I match a custom set of characters?

**A:** Use square brackets []

```python
import re

re.findall(r'[aeiou]', 'hello')     # ['e', 'o']
re.findall(r'[a-z]', 'Hello123')    # ['e', 'l', 'l', 'o']
re.findall(r'[^0-9]', 'a1b2c3')     # ['a', 'b', 'c'] (negated)
re.findall(r'[A-Za-z0-9]', 'Hi!')   # ['H', 'i']
```
