# Print to File

**Q:** How do I redirect print() to a file?

**A:** Use the file parameter

```python
with open('output.txt', 'w') as f:
    print('Hello', file=f)
    print('World', file=f)
    print(1, 2, 3, sep=', ', file=f)  # '1, 2, 3'
```

Convenient alternative to f.write() with auto newlines.
