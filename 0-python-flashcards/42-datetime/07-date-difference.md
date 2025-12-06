# Difference Between Dates

**Q:** How do I find the number of days between two dates?

**A:** Subtract dates to get timedelta, then access .days

```python
from datetime import date

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 15)
diff = d2 - d1
print(diff.days)  # 14
```
