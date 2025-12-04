# CSV to List of Dicts

**Q:** How do I read an entire CSV into a list of dictionaries?

**A:** Use list() on DictReader

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)
# data[0] = {'name': 'Alice', 'age': '30', ...}
```
