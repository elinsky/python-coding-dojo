# Wraps Decorator

**Q:** How do I preserve function metadata when writing decorators?

**A:** Use @functools.wraps()

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}"

greet.__name__  # 'greet' (not 'wrapper')
greet.__doc__   # 'Greet someone.'
```
