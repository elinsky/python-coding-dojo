# JSON Decode Error

**Q:** How do I handle invalid JSON parsing errors?

**A:** Catch json.JSONDecodeError

```python
import json

try:
    data = json.loads('{"invalid": }')
except json.JSONDecodeError as e:
    print(f"Error at line {e.lineno}, col {e.colno}: {e.msg}")
```
