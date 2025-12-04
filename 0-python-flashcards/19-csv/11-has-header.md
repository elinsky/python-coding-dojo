# CSV Detect Header

**Q:** How do I detect if a CSV file has a header row?

**A:** Use Sniffer.has_header()

```python
import csv

with open('data.csv', newline='') as f:
    sample = f.read(1024)
    has_header = csv.Sniffer().has_header(sample)
    f.seek(0)
    reader = csv.reader(f)
    if has_header:
        next(reader)  # skip header
```
