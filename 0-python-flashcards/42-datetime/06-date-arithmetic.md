# Date Arithmetic

**Q:** How do I add/subtract days from a date?

**A:** Use timedelta with + or -

```python
from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
```
