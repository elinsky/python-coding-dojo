# Write JSON File

**Q:** How do I write a Python object to a JSON file?

**A:** Use json.dump() with a file object

```python
import json

data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)
```
