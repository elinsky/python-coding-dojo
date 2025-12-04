# itemgetter vs lambda

**Q:** When should I use itemgetter instead of lambda?

**A:** itemgetter is faster (C implementation) for simple access

```python
from operator import itemgetter

# Faster - C implementation
pairs.sort(key=itemgetter(1))

# Slower - Python bytecode
pairs.sort(key=lambda x: x[1])

# For complex logic, lambda is fine
pairs.sort(key=lambda x: (x[1].lower(), -x[0]))
```
