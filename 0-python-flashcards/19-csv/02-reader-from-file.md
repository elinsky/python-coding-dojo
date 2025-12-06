# Create CSV Reader from File

**Q:** How do I create a CSV reader from a filename?

**A:**

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
```
