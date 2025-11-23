# Delete Node After Current

**Q:** How do I delete the node that comes immediately after the current node (skip over it)? What is the time complexity?

**A:** Set node.next to node.next.next. Time: O(1)

```python
node.next = node.next.next
```
