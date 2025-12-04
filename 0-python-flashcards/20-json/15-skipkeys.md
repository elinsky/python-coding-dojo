# JSON Skip Non-String Keys

**Q:** How do I handle dictionaries with non-string keys?

**A:** Use skipkeys=True to skip them (otherwise raises TypeError)

```python
import json

data = {1: 'one', 'two': 2, (3,4): 'tuple'}

json.dumps(data, skipkeys=True)
# '{"two": 2}'  - numeric key becomes string, tuple key skipped
```

Note: Integer keys are converted to strings, not skipped
