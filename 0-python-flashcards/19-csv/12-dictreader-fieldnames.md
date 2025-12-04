# DictReader Custom Fieldnames

**Q:** How do I use DictReader when the CSV has no header row?

**A:** Pass fieldnames parameter explicitly

```python
import csv

with open('no_header.csv', newline='') as f:
    reader = csv.DictReader(f, fieldnames=['name', 'age', 'city'])
    for row in reader:
        print(row['name'])
```
