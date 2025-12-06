# Writerow Format

**Q:** What format does writerow() expect?

**A:** An iterable (list, tuple, etc.)

```python
writer.writerow(['a', 'b', 'c'])  # list
writer.writerow(('a', 'b', 'c'))  # tuple
```
