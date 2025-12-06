# Create OrderedDict

**Q:** How do I create an OrderedDict?

**A:** Use collections.OrderedDict (regular dict maintains order in 3.7+)

```python
from collections import OrderedDict

d = OrderedDict()
d['first'] = 1
d['second'] = 2
```
