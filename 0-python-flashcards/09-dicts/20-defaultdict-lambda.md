# DefaultDict with Custom Factory

**Q:** How do I create a defaultdict with a custom default value?

**A:** Pass a lambda or function to defaultdict

```python
from collections import defaultdict

d = defaultdict(lambda: 42)
d = defaultdict(lambda: [0, 0])
d['new_key']  # Calls factory function
```
