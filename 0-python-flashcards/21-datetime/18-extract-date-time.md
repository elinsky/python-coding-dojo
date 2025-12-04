# Extract Date or Time from DateTime

**Q:** How do I get just the date or time from a datetime?

**A:** Use date() and time() methods

```python
from datetime import datetime

dt = datetime(2024, 1, 15, 10, 30, 45)
d = dt.date()  # date(2024, 1, 15)
t = dt.time()  # time(10, 30, 45)
```
