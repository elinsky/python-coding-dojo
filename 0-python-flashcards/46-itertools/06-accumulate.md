# Accumulate (Running Total)

**Q:** How do I compute running totals or accumulated results?

**A:** Use itertools.accumulate()

```python
from itertools import accumulate
import operator

list(accumulate([1, 2, 3, 4, 5]))
# [1, 3, 6, 10, 15] (running sum)

list(accumulate([1, 2, 3, 4], operator.mul))
# [1, 2, 6, 24] (running product)

list(accumulate([3, 1, 4, 1, 5], max))
# [3, 3, 4, 4, 5] (running max)
```
