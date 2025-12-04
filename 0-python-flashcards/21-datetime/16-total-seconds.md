# Timedelta Total Seconds

**Q:** How do I get total seconds from a timedelta?

**A:** Use total_seconds() method

```python
from datetime import timedelta

delta = timedelta(hours=2, minutes=30)
delta.total_seconds()  # 9000.0

delta = timedelta(days=1)
delta.total_seconds()  # 86400.0
```
