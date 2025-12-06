# Format DateTime to String

**Q:** How do I format a datetime as a string?

**A:** Use strftime(format)

```python
from datetime import datetime

dt = datetime(2024, 1, 15, 10, 30)
dt.strftime('%Y-%m-%d')          # '2024-01-15'
dt.strftime('%B %d, %Y')         # 'January 15, 2024'
dt.strftime('%H:%M:%S')          # '10:30:00'
dt.strftime('%Y-%m-%d %H:%M:%S') # '2024-01-15 10:30:00'
```
