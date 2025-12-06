# Get Day of Week

**Q:** How do I get the day of the week from a date?

**A:** Use weekday() (Mon=0) or isoweekday() (Mon=1)

```python
from datetime import date

d = date(2024, 1, 15)  # Monday
d.weekday()     # 0 (Mon=0, Sun=6)
d.isoweekday()  # 1 (Mon=1, Sun=7)
```
