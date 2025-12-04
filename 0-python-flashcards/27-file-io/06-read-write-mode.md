# Read and Write Mode

**Q:** How do I open a file for both reading and writing?

**A:** Add '+' to the mode

```python
# Read and write (file must exist)
with open('data.txt', 'r+') as f:
    content = f.read()
    f.write('appended')

# Write and read (truncates first)
with open('data.txt', 'w+') as f:
    f.write('hello')
    f.seek(0)
    print(f.read())  # 'hello'
```
