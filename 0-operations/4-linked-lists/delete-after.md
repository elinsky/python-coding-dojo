# Delete Node After Current

**Q:** How do I delete the node after the current node?

**A:** Set node.next to node.next.next

```python
node.next = node.next.next
```
