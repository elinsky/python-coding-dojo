# CSV Line Number

**Q:** How do I get the current line number while reading a CSV?

**A:** Use reader.line_num attribute

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"Line {reader.line_num}: {row}")
```
