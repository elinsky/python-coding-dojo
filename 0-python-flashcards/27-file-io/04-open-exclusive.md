# Open File Exclusive Create

**Q:** How do I create a file only if it doesn't exist?

**A:** Use open() with mode 'x'

```python
try:
    f = open('new_file.txt', 'x')
    f.write('Created!')
    f.close()
except FileExistsError:
    print('File already exists!')
```

'x' mode fails if file exists - prevents accidental overwrite.
