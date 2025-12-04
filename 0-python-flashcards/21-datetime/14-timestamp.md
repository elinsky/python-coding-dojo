# Unix Timestamp

**Q:** How do I convert between datetime and Unix timestamp?

**A:** Use timestamp() and fromtimestamp()

```python
from datetime import datetime

dt = datetime.now()
ts = dt.timestamp()  # 1705312200.0 (seconds since epoch)

dt = datetime.fromtimestamp(1705312200.0)
```
