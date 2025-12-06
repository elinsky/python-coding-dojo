# Compare Dates/Datetimes

**Q:** How do I compare dates and datetimes?

**A:** Use standard comparison operators

```python
from datetime import date, datetime

d1 = date(2024, 1, 15)
d2 = date(2024, 1, 20)

d1 < d2   # True
d1 == d2  # False
d1 >= d2  # False

# Sort dates
dates = [d2, d1]
sorted(dates)  # [d1, d2]
```
