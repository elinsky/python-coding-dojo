# CSV DictReader

**Q:** How do I read CSV rows as dictionaries with column headers as keys?

**A:** Use csv.DictReader() - first row becomes keys

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```
