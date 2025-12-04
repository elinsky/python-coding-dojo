# Cycle (Infinite)

**Q:** How do I cycle through an iterable infinitely?

**A:** Use itertools.cycle()

```python
from itertools import cycle, islice

colors = cycle(['red', 'green', 'blue'])
list(islice(colors, 7))
# ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']
```
