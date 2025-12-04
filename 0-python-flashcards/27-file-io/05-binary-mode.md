# Binary Mode

**Q:** How do I read/write binary files (images, etc.)?

**A:** Add 'b' to the mode

```python
# Read binary
with open('image.png', 'rb') as f:
    data = f.read()  # returns bytes

# Write binary
with open('output.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')
```

Use 'rb', 'wb', 'ab' for binary read/write/append.
