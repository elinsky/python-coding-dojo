# Aware vs Naive Datetime

**Q:** What's the difference between aware and naive datetimes?

**A:** Aware has timezone info, naive does not

```python
from datetime import datetime, timezone

# Naive - no timezone
naive = datetime(2024, 1, 15, 10, 30)
naive.tzinfo  # None

# Aware - has timezone
aware = datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)
aware.tzinfo  # timezone.utc
```

Note: Comparing aware and naive raises TypeError
