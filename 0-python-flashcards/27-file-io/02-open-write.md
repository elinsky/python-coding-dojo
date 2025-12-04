# Open File for Writing

**Q:** How do I open a file for writing (overwrites existing)?

**A:** Use open() with mode 'w'

```python
f = open('output.txt', 'w')
f.write('Hello, World!')
f.close()
```

Warning: 'w' mode truncates (erases) the file if it exists!
