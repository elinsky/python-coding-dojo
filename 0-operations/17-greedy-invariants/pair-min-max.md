# Pair Minimum with Maximum

**Q:** How do you optimally pair tasks to workers when each gets 2 tasks?

**A:** Sort tasks, pair shortest with longest, second shortest with second longest, etc.

```python
tasks.sort()
pairs = [
    (tasks[i], tasks[-(i+1)])
    for i in range(len(tasks) // 2)
]
```
