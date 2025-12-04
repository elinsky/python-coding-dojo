# Add Child to ChainMap

**Q:** How do I add a new dict to the front of a ChainMap?

**A:** Use new_child() method

```python
from collections import ChainMap

cm = ChainMap({'a': 1}, {'b': 2})
new_cm = cm.new_child({'c': 3})
# Searches: {'c': 3}, {'a': 1}, {'b': 2}
```
