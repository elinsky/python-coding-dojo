# read_text() vs open()

**Q:** When should I use p.read_text() vs open()?

**A:**

- `read_text()` - quick one-liner, loads entire file into memory
- `open()` - more control, can read line by line, needed for csv.reader/json.load
