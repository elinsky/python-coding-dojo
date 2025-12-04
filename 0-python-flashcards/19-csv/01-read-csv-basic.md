# Read CSV File Basic

**Q:** How do I read a CSV file row by row?

**A:** Use csv.reader() with newline=''

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row is a list of strings
```
