# Cached Property

**Q:** How do I cache a computed property value?

**A:** Use @functools.cached_property

```python
from functools import cached_property

class DataSet:
    def __init__(self, data):
        self._data = data

    @cached_property
    def stats(self):
        # Expensive computation, runs only once
        return {
            'mean': sum(self._data) / len(self._data),
            'max': max(self._data)
        }

ds = DataSet([1, 2, 3, 4, 5])
ds.stats  # computed
ds.stats  # cached, no recomputation
```
