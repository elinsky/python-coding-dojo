# Regex Alternation (OR)

**Q:** How do I match one pattern OR another?

**A:** Use the pipe | operator

```python
import re

re.findall(r'cat|dog', 'I have a cat and a dog')
# ['cat', 'dog']

re.search(r'(Mon|Tues|Wednes)day', 'Tuesday')
# Match for 'Tuesday'
```
