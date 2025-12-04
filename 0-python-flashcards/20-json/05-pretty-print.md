# Pretty Print JSON

**Q:** How do I format JSON with indentation for readability?

**A:** Use the indent parameter

```python
import json

data = {'name': 'Alice', 'scores': [95, 87, 92]}
print(json.dumps(data, indent=2))
# {
#   "name": "Alice",
#   "scores": [95, 87, 92]
# }
```
