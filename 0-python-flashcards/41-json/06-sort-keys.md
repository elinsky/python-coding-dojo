# Sort JSON Keys

**Q:** How do I output JSON with keys in alphabetical order?

**A:** Use sort_keys=True

```python
import json

data = {'zebra': 1, 'apple': 2, 'mango': 3}
print(json.dumps(data, sort_keys=True))
# {"apple": 2, "mango": 3, "zebra": 1}
```
