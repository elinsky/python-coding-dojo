# CSV to List of Lists

**Q:** How do I read an entire CSV into a list of lists?

**A:** Use list() on the reader

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
# data[0] is header, data[1:] are rows
```
