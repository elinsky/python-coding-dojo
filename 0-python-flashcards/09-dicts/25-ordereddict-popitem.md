# OrderedDict Pop Last or First

**Q:** How do I remove the last or first item from OrderedDict?

**A:** Use popitem(last=True/False)

```python
d.popitem(last=True)   # Remove last (LIFO)
d.popitem(last=False)  # Remove first (FIFO)
```
