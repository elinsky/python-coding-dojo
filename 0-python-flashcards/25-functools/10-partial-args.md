# Partial with Positional Args

**Q:** How does partial handle positional arguments?

**A:** Frozen args are prepended to call args

```python
from functools import partial

def greet(greeting, name, punct):
    return f"{greeting}, {name}{punct}"

# Freeze first argument
say_hello = partial(greet, "Hello")
say_hello("Alice", "!")  # "Hello, Alice!"

# Freeze multiple
say_hello_exclaim = partial(greet, "Hello", punct="!")
say_hello_exclaim("Bob")  # "Hello, Bob!"
```
