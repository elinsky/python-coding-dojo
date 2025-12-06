# Read JSON File

**Q:** How do I read and parse a JSON file?

**A:** Use json.load() with a file object

```python
import json

with open('data.json') as f:
    data = json.load(f)
```
