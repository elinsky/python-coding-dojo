# JSON NaN and Infinity

**Q:** How does json handle NaN and Infinity values?

**A:** Allowed by default, but not valid JSON - use allow_nan=False to raise error

```python
import json
import math

json.dumps({'val': math.nan})     # '{"val": NaN}' - not valid JSON!
json.dumps({'val': math.inf})     # '{"val": Infinity}'

json.dumps({'val': math.nan}, allow_nan=False)  # raises ValueError
```
