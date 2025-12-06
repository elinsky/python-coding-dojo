# Combine Date and Time

**Q:** How do I combine a date and time into a datetime?

**A:** Use datetime.combine()

```python
from datetime import date, time, datetime

d = date(2024, 1, 15)
t = time(10, 30, 0)
dt = datetime.combine(d, t)
# datetime(2024, 1, 15, 10, 30, 0)
```
