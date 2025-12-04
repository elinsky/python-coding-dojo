# Open File for Reading

**Q:** How do I open a file for reading?

**A:** Use open() with mode 'r' (default)

```python
f = open('data.txt', 'r')
content = f.read()
f.close()

# Or use 'r' explicitly
f = open('data.txt', mode='r')
```
