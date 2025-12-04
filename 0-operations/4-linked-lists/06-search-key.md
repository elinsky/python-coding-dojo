# Search for Key

**Q:** How do I search for a key in a linked list L? What is the time complexity?

**A:** Traverse while L exists and data doesn't match. Time: O(n) where n is the length of the list

```python
while L and L.data != key:
    L = L.next
return L  # None if not found
```
