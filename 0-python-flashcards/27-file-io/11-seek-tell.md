# Seek and Tell

**Q:** How do I move around in a file?

**A:** Use seek() to move, tell() to get position

```python
with open('data.txt', 'r') as f:
    f.read(10)         # read 10 chars
    pos = f.tell()     # get current position (10)

    f.seek(0)          # go to beginning
    f.seek(5)          # go to position 5
    f.seek(0, 2)       # go to end (whence=2)

# seek(offset, whence): 0=start, 1=current, 2=end
```
