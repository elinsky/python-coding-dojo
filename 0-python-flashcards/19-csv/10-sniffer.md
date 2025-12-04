# CSV Sniffer - Detect Format

**Q:** How do I automatically detect a CSV file's delimiter and format?

**A:** Use csv.Sniffer() to analyze a sample

```python
import csv

with open('unknown.csv', newline='') as f:
    sample = f.read(1024)
    dialect = csv.Sniffer().sniff(sample)
    f.seek(0)
    reader = csv.reader(f, dialect)
```
