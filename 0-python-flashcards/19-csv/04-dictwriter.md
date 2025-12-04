# CSV DictWriter

**Q:** How do I write dictionaries to a CSV file?

**A:** Use csv.DictWriter() with fieldnames and writeheader()

```python
import csv

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'NYC'})
```
