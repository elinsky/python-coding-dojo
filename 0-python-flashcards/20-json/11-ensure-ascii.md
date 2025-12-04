# JSON Non-ASCII Characters

**Q:** How do I output non-ASCII characters directly instead of escaped?

**A:** Use ensure_ascii=False

```python
import json

data = {'city': 'Zürich', 'greeting': '你好'}
json.dumps(data)
# '{"city": "Z\\u00fcrich", "greeting": "\\u4f60\\u597d"}'

json.dumps(data, ensure_ascii=False)
# '{"city": "Zürich", "greeting": "你好"}'
```
