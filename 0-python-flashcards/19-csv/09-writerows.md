# CSV Write Multiple Rows

**Q:** How do I write multiple rows at once to a CSV?

**A:** Use writerows() with an iterable of rows

```python
import csv

rows = [
    ['Alice', 30, 'NYC'],
    ['Bob', 25, 'LA'],
    ['Charlie', 35, 'Chicago']
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```
