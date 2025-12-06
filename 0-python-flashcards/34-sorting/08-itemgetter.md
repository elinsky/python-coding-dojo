# Sort with itemgetter

**Q:** How do I sort by item/index using operator.itemgetter?

**A:** Use itemgetter(index) or itemgetter(key)

```python
from operator import itemgetter

# Sort tuples by second element
pairs = [(1, 'c'), (2, 'a'), (3, 'b')]
pairs.sort(key=itemgetter(1))

# Sort dicts by key
students.sort(key=itemgetter('gpa'))

# Multiple items
data.sort(key=itemgetter(1, 2))
```
