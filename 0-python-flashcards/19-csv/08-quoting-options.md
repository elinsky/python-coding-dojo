# CSV Quoting Options

**Q:** What are the CSV quoting constants and when to use them?

**A:** Control when fields are quoted

```python
import csv

csv.QUOTE_MINIMAL   # default - quote only when needed
csv.QUOTE_ALL       # quote every field
csv.QUOTE_NONNUMERIC  # quote non-numeric, convert unquoted to float
csv.QUOTE_NONE      # never quote (must set escapechar)
```
