# Iterate Over Lines

**Q:** How do I efficiently read a file line by line?

**A:** Iterate over the file object directly

```python
with open('data.txt') as f:
    for line in f:
        print(line.strip())  # strip removes trailing \n
```

This is memory-efficient - doesn't load entire file at once.
