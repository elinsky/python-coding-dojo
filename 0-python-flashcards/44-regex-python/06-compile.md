# Compile Regex

**Q:** How do I compile a regex for reuse?

**A:**

```python
pattern = re.compile(r'pattern')
pattern.search(string_to_search)
```
