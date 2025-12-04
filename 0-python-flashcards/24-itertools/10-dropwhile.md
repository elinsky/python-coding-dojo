# Drop While

**Q:** How do I skip elements while a condition is true?

**A:** Use itertools.dropwhile()

```python
from itertools import dropwhile

list(dropwhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [5, 2, 1] - drops until first False

list(dropwhile(lambda x: x > 0, [3, 2, 1, 0, -1]))
# [0, -1]
```
