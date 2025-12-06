# OrderedDict Add to Front

**Q:** How do I add a new item to the front of an OrderedDict?

**A:** Assign then move to beginning with move_to_end(last=False)

```python
d['new_key'] = value
d.move_to_end('new_key', last=False)  # Move to front
```
