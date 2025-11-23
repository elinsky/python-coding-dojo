# Find Tail Node

**Q:** How do I find the tail (last node) of a list? What is the time complexity?

**A:** Traverse until next is None. Time: O(n) where n is the length of the list

```python
while node.next:
    node = node.next
# node is now the tail
```
