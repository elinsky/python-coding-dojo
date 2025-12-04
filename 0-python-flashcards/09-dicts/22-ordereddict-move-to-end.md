# Move OrderedDict Item to End

**Q:** How do I move an existing key to the end (or beginning) of OrderedDict?

**A:** Use move_to_end(key, last=True/False)

```python
d.move_to_end('key')  # Move to end
d.move_to_end('key', last=False)  # Move to beginning
```
