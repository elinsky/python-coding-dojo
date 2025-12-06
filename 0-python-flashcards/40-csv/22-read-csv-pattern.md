# Read CSV Pattern

**Q:** Write the full pattern to read a CSV file row by row

**A:**

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
```
