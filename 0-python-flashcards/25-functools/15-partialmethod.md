# Partial Method

**Q:** How do I use partial with class methods?

**A:** Use functools.partialmethod()

```python
from functools import partialmethod

class Cell:
    def __init__(self):
        self._alive = False

    def set_state(self, state):
        self._alive = state

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
c.set_alive()   # c._alive = True
c.set_dead()    # c._alive = False
```
