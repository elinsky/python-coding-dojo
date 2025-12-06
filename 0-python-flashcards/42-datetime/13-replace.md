# Replace Date/Time Components

**Q:** How do I create a new date/datetime with some components changed?

**A:** Use replace() - returns new object

```python
from datetime import datetime

dt = datetime(2024, 1, 15, 10, 30)
new_dt = dt.replace(year=2025)        # 2025-01-15 10:30
new_dt = dt.replace(hour=0, minute=0) # 2024-01-15 00:00
```
