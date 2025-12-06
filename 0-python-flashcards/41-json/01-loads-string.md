# Parse JSON String

**Q:** How do I parse a JSON string into a Python object?

**A:** Use json.loads() (load string)

```python
import json

data = json.loads('{"name": "Alice", "age": 30}')
# data = {'name': 'Alice', 'age': 30}
```
