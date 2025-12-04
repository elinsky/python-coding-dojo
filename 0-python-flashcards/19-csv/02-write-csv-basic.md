# Write CSV File Basic

**Q:** How do I write rows to a CSV file?

**A:** Use csv.writer() with newline=''

```python
import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'NYC'])
```
