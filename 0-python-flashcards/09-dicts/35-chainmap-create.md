# Create ChainMap

**Q:** How do I group multiple dicts into a single view?

**A:** Use collections.ChainMap

```python
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
overrides = {'user': 'admin'}
combined = ChainMap(overrides, defaults)
combined['user']   # 'admin' (from first dict)
combined['color']  # 'red' (from second dict)
```
