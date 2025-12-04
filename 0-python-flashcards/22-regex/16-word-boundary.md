# Word Boundary

**Q:** How do I match whole words only?

**A:** Use \b for word boundaries

```python
import re

re.findall(r'\bcat\b', 'cat catalog bobcat')
# ['cat']

re.findall(r'cat', 'cat catalog bobcat')
# ['cat', 'cat', 'cat']
```
