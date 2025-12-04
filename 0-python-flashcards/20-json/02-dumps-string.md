# Convert to JSON String

**Q:** How do I convert a Python object to a JSON string?

**A:** Use json.dumps() (dump string)

```python
import json

data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)
# '{"name": "Alice", "age": 30}'
```
