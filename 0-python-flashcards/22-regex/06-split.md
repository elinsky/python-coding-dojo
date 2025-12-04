# Regex Split

**Q:** How do I split a string by a regex pattern?

**A:** Use re.split()

```python
import re

re.split(r'\s+', 'hello   world  foo')
# ['hello', 'world', 'foo']

re.split(r'[,;]', 'a,b;c,d')
# ['a', 'b', 'c', 'd']
```
