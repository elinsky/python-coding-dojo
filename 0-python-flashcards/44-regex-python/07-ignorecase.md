# Case Insensitive Match

**Q:** How do I make a regex match case insensitive?

**A:**

```python
re.search(r'pattern', string_to_search, re.IGNORECASE)
```
