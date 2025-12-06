# Parse String to DateTime

**Q:** How do I parse a string into a datetime?

**A:** Use datetime.strptime(string, format)

```python
from datetime import datetime

dt = datetime.strptime('2024-01-15', '%Y-%m-%d')
dt = datetime.strptime('01/15/2024 10:30', '%m/%d/%Y %H:%M')
```
