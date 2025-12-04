# loads vs load, dumps vs dump

**Q:** What's the difference between loads/load and dumps/dump?

**A:** The 's' suffix means string; without 's' means file

```python
import json

# String operations
json.loads(string)      # parse string → Python
json.dumps(obj)         # Python → string

# File operations
json.load(file)         # parse file → Python
json.dump(obj, file)    # Python → file
```
