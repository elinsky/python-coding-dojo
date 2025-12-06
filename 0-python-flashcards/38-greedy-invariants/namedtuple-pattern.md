# Named Tuple for Greedy Results

**Q:** How do you return structured results from greedy algorithms?

**A:** Use collections.namedtuple for readable, immutable results.

```python
from collections import namedtuple

PairedTasks = namedtuple('PairedTasks', ('task_1', 'task_2'))
Interval = namedtuple('Interval', ('left', 'right'))

# Usage:
return [PairedTasks(tasks[i], tasks[-i-1])
        for i in range(len(tasks) // 2)]
```
