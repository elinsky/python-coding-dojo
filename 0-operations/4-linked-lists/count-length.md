# Count List Length

**Q:** How do I count the length of a linked list (requires multiple lines)? What is the time complexity?

**A:** Traverse and increment counter. Time: O(n) where n is the length of the list

```python
length = 0
while L:
    length += 1
    L = L.next
```
