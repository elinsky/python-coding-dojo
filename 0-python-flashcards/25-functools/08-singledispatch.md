# Single Dispatch

**Q:** How do I create overloaded functions based on argument type?

**A:** Use @functools.singledispatch

```python
from functools import singledispatch

@singledispatch
def process(arg):
    print(f"Default: {arg}")

@process.register(int)
def _(arg):
    print(f"Integer: {arg * 2}")

@process.register(list)
def _(arg):
    print(f"List length: {len(arg)}")

process("hello")  # Default: hello
process(5)        # Integer: 10
process([1,2,3])  # List length: 3
```
