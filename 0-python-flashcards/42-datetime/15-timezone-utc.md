# UTC Timezone

**Q:** How do I work with UTC timezone?

**A:** Use timezone.utc or datetime.now(timezone.utc)

```python
from datetime import datetime, timezone

# Current time in UTC
utc_now = datetime.now(timezone.utc)

# Create aware datetime in UTC
dt = datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)
```
