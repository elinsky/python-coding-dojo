# Create DictWriter

**Q:** How do I write dictionaries to a CSV file?

**A:**

```python
import csv

writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
```
