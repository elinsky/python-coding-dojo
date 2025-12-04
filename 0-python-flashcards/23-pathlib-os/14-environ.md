# Environment Variables

**Q:** How do I access environment variables?

**A:** Use os.environ dict

```python
import os

home = os.environ['HOME']
path = os.environ.get('MY_VAR', 'default')

# Set an environment variable
os.environ['MY_VAR'] = 'value'
```
