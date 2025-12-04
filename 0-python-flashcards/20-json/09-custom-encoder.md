# Custom JSON Encoder

**Q:** How do I serialize custom objects (like datetime) to JSON?

**A:** Use the default parameter or subclass JSONEncoder

```python
import json
from datetime import datetime

def custom_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")

data = {'timestamp': datetime.now()}
json.dumps(data, default=custom_encoder)
```
