# ISO Format

**Q:** How do I convert datetime to/from ISO 8601 format?

**A:** Use isoformat() and fromisoformat()

```python
from datetime import datetime

dt = datetime(2024, 1, 15, 10, 30, 0)
iso_str = dt.isoformat()  # '2024-01-15T10:30:00'

dt = datetime.fromisoformat('2024-01-15T10:30:00')
```
