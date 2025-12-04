# Access ChainMap Parents

**Q:** How do I access underlying dicts in a ChainMap?

**A:** Use maps attribute or parents property

```python
from collections import ChainMap

cm = ChainMap({'a': 1}, {'b': 2}, {'c': 3})
cm.maps  # [{'a': 1}, {'b': 2}, {'c': 3}]
cm.parents  # ChainMap({'b': 2}, {'c': 3})
```
