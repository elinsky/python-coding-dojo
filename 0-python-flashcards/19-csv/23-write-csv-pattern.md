# Write CSV Pattern

**Q:** Write the full pattern to write rows to a CSV file

**A:**

```python
import csv

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])  # header
    writer.writerow(['Alice', 30, 'NYC'])
```
