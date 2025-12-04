# Skip CSV Header Row

**Q:** How do I skip the header row when reading a CSV?

**A:** Use next() to consume the first row

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        print(row)
```
