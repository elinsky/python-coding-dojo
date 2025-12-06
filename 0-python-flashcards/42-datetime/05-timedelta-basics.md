# Timedelta Basics

**Q:** How do I represent a duration of time?

**A:** Use timedelta with days, seconds, hours, minutes, weeks

```python
from datetime import timedelta

delta = timedelta(days=7)
delta = timedelta(hours=2, minutes=30)
delta = timedelta(weeks=1, days=3)
```
