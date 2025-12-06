# Custom JSON Decoder

**Q:** How do I transform JSON objects during parsing?

**A:** Use object_hook parameter

```python
import json
from datetime import datetime

def custom_decoder(d):
    if 'timestamp' in d:
        d['timestamp'] = datetime.fromisoformat(d['timestamp'])
    return d

data = json.loads('{"timestamp": "2024-01-15T10:30:00"}',
                  object_hook=custom_decoder)
```
