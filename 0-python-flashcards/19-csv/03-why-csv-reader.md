# Why CSV Reader

**Q:** Why use csv.reader instead of reading a file line by line?

**A:**

- Splits each line by delimiter into fields
- Handles quoted fields (e.g., `"hello, world"` stays as one field)
- Handles newlines inside quoted fields
- Returns each row as a list of strings
