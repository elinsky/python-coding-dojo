# Sort by String Length

**Q:** How do I sort strings by length?

**A:** Use len as key function

```python
words = ['apple', 'pie', 'x', 'banana']
words.sort(key=len)  # ['x', 'pie', 'apple', 'banana']
```
