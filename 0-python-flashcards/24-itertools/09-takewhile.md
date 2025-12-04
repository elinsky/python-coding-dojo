# Take While

**Q:** How do I take elements while a condition is true?

**A:** Use itertools.takewhile()

```python
from itertools import takewhile

list(takewhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [1, 3] - stops at first False

list(takewhile(lambda x: x > 0, [3, 2, 1, 0, -1]))
# [3, 2, 1]
```
