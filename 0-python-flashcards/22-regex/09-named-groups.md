# Regex Named Groups

**Q:** How do I use named capture groups?

**A:** Use (?P<name>...) syntax

```python
import re

m = re.search(r'(?P<area>\d{3})-(?P<number>\d{4})', '123-4567')
m.group('area')    # '123'
m.group('number')  # '4567'
m.groupdict()      # {'area': '123', 'number': '4567'}
```
