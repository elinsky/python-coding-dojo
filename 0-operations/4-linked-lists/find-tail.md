# Find Tail Node

**Q:** How do I find the tail (last node) of a list?

**A:** Traverse until next is None

```python
while node.next:
    node = node.next
# node is now the tail
```
