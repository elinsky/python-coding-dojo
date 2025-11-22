# Insert Node After Current

**Q:** How do I insert a new_node after an existing node?

**A:** Set new_node.next to node.next, then update node.next

```python
new_node.next = node.next
node.next = new_node
```
