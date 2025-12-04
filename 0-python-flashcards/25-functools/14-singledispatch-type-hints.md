# Singledispatch with Type Hints

**Q:** How do I use type hints with singledispatch?

**A:** Use type hints in the function signature (Python 3.7+)

```python
from functools import singledispatch

@singledispatch
def process(arg):
    raise NotImplementedError(f"No handler for {type(arg)}")

@process.register
def _(arg: int):
    return arg * 2

@process.register
def _(arg: str):
    return arg.upper()

process(5)       # 10
process("hello") # 'HELLO'
```
