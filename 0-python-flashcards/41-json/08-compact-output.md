# Compact JSON Output

**Q:** How do I produce the most compact JSON output?

**A:** Use separators=(',', ':') to remove whitespace

```python
import json

data = {'a': 1, 'b': 2}
json.dumps(data, separators=(',', ':'))
# '{"a":1,"b":2}'

# vs default:
# '{"a": 1, "b": 2}'
```
