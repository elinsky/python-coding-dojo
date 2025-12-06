# Get Environment Variable

**Q:** How do I access an environment variable?

**A:**

```python
import os

os.environ['HOME']
os.environ.get('MY_VAR', 'default')
```
