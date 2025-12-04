# CSV Custom Delimiter

**Q:** How do I read/write CSV with a different delimiter (e.g., tab, pipe)?

**A:** Use the delimiter parameter

```python
import csv

# Tab-delimited
with open('data.tsv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')

# Pipe-delimited
with open('data.txt', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='|')
```
