# Sort Strings Case-Insensitive

**Q:** How do I sort strings ignoring case?

**A:** Use str.lower or str.casefold as key

```python
words = ['Apple', 'banana', 'Cherry']
words.sort(key=str.lower)
words.sort(key=str.casefold)  # Better for Unicode
```
