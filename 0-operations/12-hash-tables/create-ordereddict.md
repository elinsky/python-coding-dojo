# Create OrderedDict

**Q:** How do I create a dictionary that maintains insertion order? What is the time complexity?

**A:** Use collections.OrderedDict (Note: regular dict maintains order in Python 3.7+). Time: O(1)

```python
from collections import OrderedDict

d = OrderedDict()
d['first'] = 1
d['second'] = 2
```
