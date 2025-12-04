# Open File for Appending

**Q:** How do I open a file to add content at the end?

**A:** Use open() with mode 'a'

```python
f = open('log.txt', 'a')
f.write('New log entry\n')
f.close()
```

Creates file if it doesn't exist; adds to end if it does.
