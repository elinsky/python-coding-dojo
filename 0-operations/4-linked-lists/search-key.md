# Search for Key

**Q:** How do I search for a key in a linked list L?

**A:** Traverse while L exists and data doesn't match

```python
while L and L.data != key:
    L = L.next
return L  # None if not found
```
