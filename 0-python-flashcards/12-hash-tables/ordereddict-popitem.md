# OrderedDict Pop Last or First

**Q:** How do I remove and return the last or first item from OrderedDict? What is the time complexity?

**A:** Use popitem(last=True/False). Time: O(1)

```python
d.popitem(last=True)   # Remove last item (LIFO)
d.popitem(last=False)  # Remove first item (FIFO)
```
