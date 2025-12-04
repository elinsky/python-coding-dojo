# Move OrderedDict Item to End

**Q:** How do I move an existing key to the end (or beginning) of OrderedDict? What is the time complexity?

**A:** Use move_to_end(key, last=True/False). Time: O(1)

```python
d.move_to_end('key')  # Move to end (most recent)
d.move_to_end('key', last=False)  # Move to beginning
```
