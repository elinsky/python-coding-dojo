# Count List Length

**Q:** How do I count the length of a linked list?

**A:** Traverse and increment counter

```python
length = 0
while L:
    length += 1
    L = L.next
```
